
# ======================== Class Player =======================================
class Player:
	# student do not allow to change two first functions
	def __init__(self, str_name):
		self.str = str_name

	def __str__(self):
		return self.str

	# Student MUST implement this function
	# The return value should be a move that is denoted by a list of tuples:
	# [(row1, col1), (row2, col2), (row3, col3)] with:
	# (row1, col1): current position of selected amazon
	# (row2, col2): new position of selected amazon
	# (row3, col3): position of the square is shot
	def nextMove(self, state):
		result = [(0,3),(5,3),(8,6)] # example move in wikipedia
		return result

WQUEEN=1
BQUEEN=2
ARRROW=3
FREE=0
ROW=10
COLUMN=10
class Board:
	#Conver State(in main) to Board
	def __init__(self,board):
		self.board=[]
		self.whitePositions=[]
		self.blackPositions=[]
		self.whiteTraps=[]
		self.blackTraps=[]
		self.heuristicValue=None
		for i in range(0,ROW):
			for j in range(0,COLUMN):
				if board[i][j]=='.':
					self.board[i][j]=FREE
				elif board[i][j]=='X':
					self.board[i][j]=ARRROW
				elif board[i][j]=='b':
					self.board[i][j]=BQUEEN
					self.blackPositions.__add__((i,j))
				elif board[i][j]=='w':
					self.board[i][j]=WQUEEN
					self.whitePositions.__add__((i,j))
	def copyBoard(self):
		return self.deepcopy()

	def freeSquare(self,x,y):
		self.board[x][y]=FREE

	#piece=WQUEEN || piece=BQUEEN || piece=FREE ||piece=ARROW
	def placeMarker(self,x,y,piece):
		self.board[x][y]=piece

	def isMarked(self,x,y):
		if self.board[x][y]==FREE:
			return False
		else:
			return True

	def getPiece(self,x,y):
		return self.board[x][y]

	def whitePieceTrapped(self,x,y):
		return (x,y) in self.whiteTraps

	def blackPieceTrapped(self,x,y):
		return (x,y) in self.blackTraps

	def addWhiteTrappedPiece(self,x,y):
		self.whiteTraps.append((x,y))

	def addBlackTrappedPiece(self,x,y):
		self.blackTraps.append((x,y))

	def clearWhiteTrapMap(self):
		self.whiteTraps.clear()

	def clearBlackTrapMap(self):
		self.blackTraps.clear()

	def updateWhitePositions(self,oldX,oldY,newX,newY):
		for i in self.whitePositions:
			if(i==(oldX,oldY)):
				i=(oldX,oldY)
				return

	def updateBlackPositions(self,oldX,oldY,newX,newY):
		for i in self.blackPositions:
			if(i==(oldX,oldY)):
				i=(oldX,oldY)
				return

	def getWhitePositions(self):
		return self.whitePositions

	def getBlackPositions(self):
		return self.blackPositions

	#Nguy Hiểm
	def getBoard(self):
		return self

	def getBlackTrappedPieces(self):
		return self.blackTraps

	def getWhiteTrappedPieces(self):
		return self.blackTraps

	def setHeuristicValue(self,value):
		self.heuristicValue=value

	def getHeuristicValue(self):
		return self.heuristicValue