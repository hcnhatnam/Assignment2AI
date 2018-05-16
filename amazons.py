
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
		a=Board(state)
		board_print(a.board)
		result = [(0,3),(5,3),(8,6)] # example move in wikipedia
		return result

def board_print(board):

	for i in [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]:
		print(i, ":", end=" ")
		for j in range(10):
			print(board[i][j], end=" ")
		print()
	print("   ", 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
	print("")

WQUEEN=1
BQUEEN=2
ARRROW=3
FREE=0
ROW=10
COLUMN=10
class Board:
	#Conver State(in main) to Board
	def __init__(self,board):
		self.board=[[0 for x in range(10)] for y in range(10)]
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
					self.blackPositions.append((i,j))
				elif board[i][j]=='w':
					self.board[i][j]=WQUEEN
					self.whitePositions.append((i,j))
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

	def hashCode(self):
		return hash(str(self.board))
class Actions:
	def __init__(self):
		self.leftOne = [ -1, 0 ]
		self.leftTwo = [ -2, 0 ]
		self.leftThree = [ -3, 0 ]
		self.leftFour = [ -4, 0 ]
		self.leftFive = [ -5, 0 ]
		self.leftSix = [ -6, 0 ]
		self.leftSeven = [ -7, 0 ]
		self.leftEight = [ -8, 0 ]
		self.leftNine = [ -9, 0 ]

		self.rightOne = [ 1, 0 ]
		self.rightTwo = [ 2, 0 ]
		self.rightThree = [ 3, 0 ]
		self.rightFour = [ 4, 0 ]
		self.rightFive = [ 5, 0 ]
		self.rightSix = [ 6, 0 ]
		self.rightSeven = [ 7, 0 ]
		self.rightEight = [ 8, 0 ]
		self.rightNine = [ 9, 0 ]

		self.upOne = [ 0, -1 ]
		self.upTwo = [ 0, -2 ]
		self.upThree = [ 0, -3 ]
		self.upFour = [ 0, -4 ]
		self.upFive = [ 0, -5 ]
		self.upSix = [ 0, -6 ]
		self.upSeven = [ 0, -7 ]
		self.upEight = [ 0, -8 ]
		self.upNine = [ 0, -9 ]

		self.downOne = [ 0, 1 ]
		self.downTwo = [ 0, 2 ]
		self.downThree = [ 0, 3 ]
		self.downFour = [ 0, 4 ]
		self.downFive = [ 0, 5 ]
		self.downSix = [ 0, 6 ]
		self.downSeven = [ 0, 7 ]
		self.downEight = [ 0, 8 ]
		self.downNine = [ 0, 9 ]

		self.downLeftOne = [ -1, -1 ]
		self.downLeftTwo = [ -2, -2 ]
		self.downLeftThree = [ -3, -3 ]
		self.downLeftFour = [ -4, -4 ]
		self.downLeftFive = [ -5, -5 ]
		self.downLeftSix = [ -6, -6 ]
		self.downLeftSeven = [ -7, -7 ]
		self.downLeftEight = [ -8, -8 ]
		self.downLeftNine = [ -9, -9 ]

		self.downRightOne = [ -1, 1 ]
		self.downRightTwo = [ -2, 2 ]
		self.downRightThree = [ -3, 3 ]
		self.downRightFour = [ -4, 4 ]
		self.downRightFive = [ -5, 5 ]
		self.downRightSix = [ -6, 6 ]
		self.downRightSeven = [ -7, 7 ]
		self.downRightEight = [ -8, 8 ]
		self.downRightNine = [ -9, 9 ]

		self.upRightOne = [ 1, 1 ]
		self.upRightTwo = [ 2, 2 ]
		self.upRightThree = [ 3, 3 ]
		self.upRightFour = [ 4, 4 ]
		self.upRightFive = [ 5, 5 ]
		self.upRightSix = [ 6, 6 ]
		self.upRightSeven = [ 7, 7 ]
		self.upRightEight = [ 8, 8 ]
		self.upRightNine = [ 9, 9 ]

		self.upLeftOne = [ 1, -1 ]
		self.upLeftTwo = [ 2, -2 ]
		self.upLeftThree = [ 3, -3 ]
		self.upLeftFour = [ 4, -4 ]
		self.upLeftFive = [ 5, -5 ]
		self.upLeftSix = [ 6, -6 ]
		self.upLeftSeven = [ 7, -7 ]
		self.upLeftEight = [ 8, -8 ]
		self.upLeftNine = [ 9, -9 ]

		self.actions = []
		self.actions.append(self.upRightNine)
		self.actions.append(self.upLeftNine)
		self.actions.append(self.upNine)
		self.actions.append(self.leftNine)
		self.actions.append(self.rightNine)
		self.actions.append(self.downNine)
		self.actions.append(self.downLeftNine)
		self.actions.append(self.downRightNine)

		self.actions.append(self.upRightEight)
		self.actions.append(self.upLeftEight)
		self.actions.append(self.upEight)
		self.actions.append(self.leftEight)
		self.actions.append(self.rightEight)
		self.actions.append(self.downEight)
		self.actions.append(self.downLeftEight)
		self.actions.append(self.downRightEight)

		self.actions.append(self.upRightSeven)
		self.actions.append(self.upLeftSeven)
		self.actions.append(self.upSeven)
		self.actions.append(self.leftSeven)
		self.actions.append(self.rightSeven)
		self.actions.append(self.downSeven)
		self.actions.append(self.downLeftSeven)
		self.actions.append(self.downRightSeven)

		self.actions.append(self.upRightSix)
		self.actions.append(self.upLeftSix)
		self.actions.append(self.upSix)
		self.actions.append(self.leftSix)
		self.actions.append(self.rightSix)
		self.actions.append(self.downSix)
		self.actions.append(self.downLeftSix)
		self.actions.append(self.downRightSix)

		self.actions.append(self.upRightFive)
		self.actions.append(self.upLeftFive)
		self.actions.append(self.upFive)
		self.actions.append(self.leftFive)
		self.actions.append(self.rightFive)
		self.actions.append(self.downFive)
		self.actions.append(self.downLeftFive)
		self.actions.append(self.downRightFive)

		self.actions.append(self.upRightFour)
		self.actions.append(self.upLeftFour)
		self.actions.append(self.leftFour)
		self.actions.append(self.upFour)
		self.actions.append(self.rightFour)
		self.actions.append(self.downFour)
		self.actions.append(self.downLeftFour)
		self.actions.append(self.downRightFour)

		self.actions.append(self.upRightThree)
		self.actions.append(self.upLeftThree)
		self.actions.append(self.upThree)
		self.actions.append(self.leftThree)
		self.actions.append(self.rightThree)
		self.actions.append(self.downThree)
		self.actions.append(self.downLeftThree)
		self.actions.append(self.downRightThree)

		self.actions.append(self.upRightTwo)
		self.actions.append(self.upLeftTwo)
		self.actions.append(self.upTwo)
		self.actions.append(self.leftTwo)
		self.actions.append(self.rightTwo)
		self.actions.append(self.downTwo)
		self.actions.append(self.downLeftTwo)
		self.actions.append(self.downRightTwo)

		self.actions.append(self.upRightOne)
		self.actions.append(self.upLeftOne)
		self.actions.append(self.upOne)
		self.actions.append(self.leftOne)
		self.actions.append(self.rightOne)
		self.actions.append(self.downOne)
		self.actions.append(self.downLeftOne)
		self.actions.append(self.downRightOne)

		self.arrowThrows = []
		self.arrowThrows.append(self.upLeftNine)
		self.arrowThrows.append(self.upLeftEight)
		self.arrowThrows.append(self.upLeftSeven)
		self.arrowThrows.append(self.upLeftSix)
		self.arrowThrows.append(self.upLeftFive)
		self.arrowThrows.append(self.upLeftFour)
		self.arrowThrows.append(self.upLeftThree)
		self.arrowThrows.append(self.upLeftTwo)
		self.arrowThrows.append(self.upLeftOne)

		self.arrowThrows.append(self.upRightNine)
		self.arrowThrows.append(self.upRightEight)
		self.arrowThrows.append(self.upRightSeven)
		self.arrowThrows.append(self.upRightSix)
		self.arrowThrows.append(self.upRightFive)
		self.arrowThrows.append(self.upRightFour)
		self.arrowThrows.append(self.upRightThree)
		self.arrowThrows.append(self.upRightTwo)
		self.arrowThrows.append(self.upRightOne)

		self.arrowThrows.append(self.leftNine)
		self.arrowThrows.append(self.leftEight)
		self.arrowThrows.append(self.leftSeven)
		self.arrowThrows.append(self.leftSix)
		self.arrowThrows.append(self.leftFive)
		self.arrowThrows.append(self.leftFour)
		self.arrowThrows.append(self.leftThree)
		self.arrowThrows.append(self.leftTwo)
		self.arrowThrows.append(self.leftOne)

		self.arrowThrows.append(self.rightNine)
		self.arrowThrows.append(self.rightEight)
		self.arrowThrows.append(self.rightSeven)
		self.arrowThrows.append(self.rightSix)
		self.arrowThrows.append(self.rightFive)
		self.arrowThrows.append(self.rightFour)
		self.arrowThrows.append(self.rightThree)
		self.arrowThrows.append(self.rightTwo)
		self.arrowThrows.append(self.rightOne)

		self.arrowThrows.append(self.upNine)
		self.arrowThrows.append(self.upEight)
		self.arrowThrows.append(self.upSeven)
		self.arrowThrows.append(self.upSix)
		self.arrowThrows.append(self.upFive)
		self.arrowThrows.append(self.upFour)
		self.arrowThrows.append(self.upThree)
		self.arrowThrows.append(self.upTwo)
		self.arrowThrows.append(self.upOne)

		self.arrowThrows.append(self.downNine)
		self.arrowThrows.append(self.downEight)
		self.arrowThrows.append(self.downSeven)
		self.arrowThrows.append(self.downSix)
		self.arrowThrows.append(self.downFive)
		self.arrowThrows.append(self.downFour)
		self.arrowThrows.append(self.downThree)
		self.arrowThrows.append(self.downTwo)
		self.arrowThrows.append(self.downOne)

		self.arrowThrows.append(self.downLeftNine)
		self.arrowThrows.append(self.downLeftEight)
		self.arrowThrows.append(self.downLeftSeven)
		self.arrowThrows.append(self.downLeftSix)
		self.arrowThrows.append(self.downLeftFive)
		self.arrowThrows.append(self.downLeftFour)
		self.arrowThrows.append(self.downLeftThree)
		self.arrowThrows.append(self.downLeftTwo)
		self.arrowThrows.append(self.downLeftOne)

		self.arrowThrows.append(self.downRightNine)
		self.arrowThrows.append(self.downRightEight)
		self.arrowThrows.append(self.downRightSeven)
		self.arrowThrows.append(self.downRightSix)
		self.arrowThrows.append(self.downRightFive)
		self.arrowThrows.append(self.downRightFour)
		self.arrowThrows.append(self.downRightThree)
		self.arrowThrows.append(self.downRightTwo)
		self.arrowThrows.append(self.downRightOne)

		self.testMoves = []
		self.testMoves.append(self.upOne)
		self.testMoves.append(self.upRightOne)
		self.testMoves.append(self.rightOne)
		self.testMoves.append(self.downRightOne)
		self.testMoves.append(self.downOne)
		self.testMoves.append(self.downLeftOne)
		self.testMoves.append(self.leftOne)
		self.testMoves.append(self.upLeftOne)

	#Tra ve tat ca cac buoc di chuyen co the co
	def getActions(self):
		return self.actions

	#Tra ve tat ca cac buoc ban co the co
	def getArrowThrows(self):
		return self.arrowThrows

	#Tra ve 8 buoc di chuyen(1 o)
	def getSimpleMoves(self):
		return self.testMoves

class GameTreeSearch:
	def __int__(self):
		self.actions = Actions()

	def moveIsValid(self,board:Board, sX, sY, dX, dY):
		if dX < 0 or dX > 9:
			return False
		if dY < 0 or dY > 9:
			return False
		# Kiem tra buoc di chuyen theo chieu ngang
		if sX == dX:
			if sY == dY:
				return False
			# He so dieu chinh
			deltaY = dY - sY
			deltaY = deltaY / abs(deltaY)

			while(sY != dY):
				sY += deltaY
				if (board.isMarked(dX,sY)):
					return False
			return True

		# Kiem tra buoc di chuyen theo chieu doc
		if (sY == dY):
			deltaX = dX - sX
			deltaX = deltaX / abs(deltaX)
			while (sX != dX):
				sX += deltaX
				if (board.isMarked(sX, dY)):
					return False
			return True

		# Tranh di chu L
		if (abs(sX - dX) != abs(sY - dY)):
			return False

		# Kiem tra cheo hop le
		if (sX > dX and sY > dY) or (sX < dX and sY < dY):
			return self.oppositeDiagonal1(board, sX, sY, dX, dY)
		else:
			return self.oppositeDiagonal(board, sX, sY, dX, dY)

	def oppositeDiagonal1(self, board:Board, sX, sY, dX, dY):
		deltaX = dX - sX
		deltaX = deltaX/abs(deltaX)
		deltaY = deltaX

		while sX != dX or sY != dY:
			sX += deltaX
			sY += deltaY
			if (board.isMarked(sX, sY)):
				return False
		return True

	def oppositeDiagonal(self, board:Board, sX, sY, dX, dY):
		deltaX = dX - sX
		deltaX = deltaX/abs(deltaX)

		deltaY = deltaX/(-1)

		while sX != dX or sY != dY:
			sX += deltaX
			sY += deltaY
			if (board.isMarked(sX, sY)):
				return False
		return True;