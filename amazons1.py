import copy
import time
import sys
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
		ti=Timer(time.time(),1)
		currentBoard=Board(state)
		moveChoice = []
		if self.str == 'w':
			moveChoice = HMinimaxSearch(EvaluationFunction(WQUEEN), ti).alphaBetaSearch(currentBoard, WQUEEN)
		else:
			moveChoice = HMinimaxSearch(EvaluationFunction(BQUEEN), ti).alphaBetaSearch(currentBoard, BQUEEN)
		if not moveChoice:
			return []
		else:
			return [(moveChoice[0],moveChoice[1]),(moveChoice[2],moveChoice[3]),(moveChoice[4],moveChoice[5])]


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
ARROW=3
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
					self.board[i][j]=ARROW
				elif board[i][j]=='b':
					self.board[i][j]=BQUEEN
					self.blackPositions.append((i,j))
				elif board[i][j]=='w':
					self.board[i][j]=WQUEEN
					self.whitePositions.append((i,j))

	def copyBoard(self):
		return copy.deepcopy(self)

	def freeSquare(self,x,y):
		self.board[x][y]=FREE

	#piece=WQUEEN || piece=BQUEEN || piece=FREE ||piece=ARROW
	def placeMarker(self,x,y,piece):
		self.board[x][y]=piece

	def isMarked(self,x,y):
		if self.board[int(x)][int(y)]==FREE:
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
	def __init__(self):
		self.actions = Actions()

	def getActions(self):
		return self.actions

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
		return True

class SuccessorGenerator(GameTreeSearch):
	def __init__(self):
		GameTreeSearch.__init__(self)
	# Sinh tat ca cac buoc di chuyen co the cua player tu board hien tai
	def getRelevantActions(self, board:Board, player):
		moveList = [[],[],[],[]]
		piece = 0
		amazons = []
		if player == 1:
			amazons = board.getWhitePositions()
		else:
			amazons = board.getBlackPositions()

		# Duyet qua tat cac cac con hau cua player
		for amazon in amazons:
			fromX = amazon[0]
			fromY = amazon[1]

			for amazoneMove in self.getActions().getActions():
				# Tao board moi de kiem tra
				tempBoard = board.copyBoard()

				toX = fromX + amazoneMove[0]
				toY = fromY + amazoneMove[1]

				# Update vi tri quan co sau khi di chuyen
				if player == 1:
					tempBoard.updateWhitePositions(fromX, fromY, toX, toY)
				else:
					tempBoard.updateBlackPositions(fromX, fromY, toX, toY)

				# Kiem tra buoc di chuyen hop le
				if self.moveIsValid(tempBoard, fromX, fromY, toX, toY):
					tempBoard.freeSquare(fromX, fromY)
					tempBoard.placeMarker(toX, toY, player)

					# Duyet qua tat ca cac vi tri de ban
					for arrowspot in self.actions.getArrowThrows():
						arrowX = toX + arrowspot[0]
						arrowY = toY + arrowspot[1]

						if self.moveIsValid(tempBoard, toX, toY, arrowX, arrowY):
							move = [fromX, fromY, toX, toY, arrowX, arrowY]
							moveList[piece].append(move)
			piece += 1

		# Sort
		moveList.sort(key = lambda x: x.__len__())

		# Append tat ca cac buoc di chuyen vao main list
		orderedMoves = [item for sublist in moveList for item in sublist]

		return orderedMoves


	# Ham sinh con: Tao ra 1 board moi sau khi thuc hien mot buoc di chuyen move tu board hien tai
	def generateSuccessor(self, parent:Board, move, player):
		child = parent.copyBoard()
		# Cap nhat lai vi tri
		child.freeSquare(move[0], move[1])
		child.placeMarker(move[2], move[3], player)
		child.placeMarker(move[4], move[5], ARROW)

		# Cap nhat danh sach vi tri moi cua con hau cua player
		if player == 1:
			child.updateWhitePositions(move[0], move[1], move[2], move[3])
		else:
			child.updateBlackPositions(move[0], move[1], move[2], move[3])
		return child

class Timer:
	def __init__(self,startTime,MAXSEARCHTIME):
		self.startTime=startTime
		self.MAXSEARCHTIME=MAXSEARCHTIME

	def almostExpired(self):
		currentTime = time.time() - self.startTime
		if currentTime > self.MAXSEARCHTIME:
			return True
		return False

class EvaluationFunction:
	def __init__(self,role):
		self.actions=Actions()
		self.OURCOLOUR=role
		self.OPPONENT=0
		if self.OURCOLOUR == WQUEEN:
			self.OPPONENT = BQUEEN
		else:
			self.OPPONENT = WQUEEN
		self.search=GameTreeSearch()
	def evaluate(self,board,player):
		wUtility=0
		bUtility=0

		wPositions=board.getWhitePositions()
		bPositions=board.getBlackPositions()

		wDistanceTable=[[sys.maxsize for i in range(COLUMN)] for j in range(ROW)]
		bDistanceTable=[[sys.maxsize for i in range(COLUMN)] for j in range(ROW)]

		for pair in wPositions:
				wDistanceTable[pair[0]][pair[1]]=-1

		for pair in bPositions:
			bDistanceTable[pair[0]][pair[1]]=-1

		self.findDistances(board, WQUEEN, wDistanceTable)
		self.findDistances(board, BQUEEN, bDistanceTable)
		for indexRow in range(ROW):
			for indexColumn in range(COLUMN):
				if wDistanceTable[indexRow][indexColumn]>bDistanceTable[indexRow][indexColumn]:
					bUtility+=1
				if wDistanceTable[indexRow][indexColumn]<bDistanceTable[indexRow][indexColumn]:
					wUtility+=1
		adjustment = self.adjustForIsolatedPieces(board)
		if player == 1:
			return wUtility + adjustment - bUtility
		else:
			return bUtility + adjustment - wUtility
	#Tinh toan khoang cach
	def findDistances(seft,board:Board, player, distanceTable):
		positions=[]
		queue=[]
		if player==WQUEEN:
			positions=board.getWhitePositions()
		else:
			positions=board.getBlackPositions()

		for pair in positions:
			queue.append(pair)

		while not queue:
			top=queue.pop(0)
			xPos=top[0]
			yPos=top[1]
			for action in seft.actions:
				currentDistance = distanceTable[xPos][yPos]
				if currentDistance == -1:
					currentDistance = 0
				newX=xPos+action[0]
				newY=yPos+action[1]
				if (newX > 9 or newX < 0) or (newY > 9 or newY < 0):
					continue

				currentDistance+=1
				if not board.isMarked(newX,newY):
					if seft.search.moveIsValid(board,xPos,yPos,newX,newY):
						if distanceTable[newX][newY]>currentDistance:
							distanceTable[newX][newY]=currentDistance
							queue.insert(0,(newX,newY))
	#Tao he so dieu chinh de +- vao ham luong gia(evaluate)
	def adjustForIsolatedPieces(self,board):
		adjustment=0
		wPositions = board.getWhitePositions()
		bPositions = board.getBlackPositions()
		whiteMoves=[True,True,True,True]
		blackMoves=[True,True,True,True]
		#Kiem tra trap cua qua mau trang
		for index in range(4):
			#kiem tra amazon co bi trap khong?
			if not  board.whitePieceTrapped(wPositions[index][0],wPositions[index][1]):
				whiteMoves[index]=self.canMove(board,wPositions[index])
				if not whiteMoves[index]:
					board.addWhiteTrappedPiece()

		#Kiem tra trap cua qua mau den
		for index in range(4):
			#kiem tra amazon co bi trap khong?
			if not  board.blackPieceTrapped(bPositions[index][0],bPositions[index][1]):
				blackMoves[index]=self.canMove(board,bPositions[index])
				if not blackMoves[index]:
					board.addBlackTrappedPiece()

		if self.OURCOLOUR == WQUEEN:
			for b in whiteMoves:
				if not b:
					adjustment -= 2
			for b in blackMoves:
				if not b:
					adjustment += 2
		else:
			for b in whiteMoves:
				if not b:
					adjustment += 2
			for b in blackMoves:
				if not b:
					adjustment -= 2
		return adjustment

	#Kiem tra quan co amzon co the di chuyen hay khong
	def canMove(self,board:Board,amazon):
		moves=self.actions.getSimpleMoves()
		for step in moves:
			testX=amazon[0]+step[0]
			testY=amazon[1]+step[1]
			if (testX >= 0 and testX < 10) and (testY >= 0 and testY < 10):
				return True
			if not board.isMarked(testX, testY):
				return True
		return False

class HMinimaxSearch:
	def __init__(self, evaluator: EvaluationFunction, timer:Timer):
		self.evaluator = evaluator
		self.DEPTH = None
		self.ourPlayer = None
		self.opponent = None
		self.scg = SuccessorGenerator()
		self.timer = timer
		self.ABSOLUTEDEPTH = 12
		self.tableSize = 0
		self.moveCount = 0
		self.ALPHA = -sys.maxsize -1
		self.BETA = sys.maxsize
		# Since there are so many collisions we can store a list, check each pair
		self.transitionTable = dict()
		self.cacheHits = 0
		self.ties = []


	def alphaBetaSearch(self, board:Board, player):
		maximum = -sys.maxsize-1
		move = None
		self.cacheHits = 0
		self.ourPlayer = player
		if self.ourPlayer == 1:
			self.opponent = 2
		else:
			self.opponent = 1

		if self.tableSize > 2000000:
			self.transitionTable.clear()
			self.tableSize = 0

		board.clearWhiteTrapMap()
		board.clearBlackTrapMap()


		self.evaluator.adjustForIsolatedPieces(board)
		self.DEPTH = 1
		searchDepth = self.DEPTH

		potentialActions = self.scg.getRelevantActions(board, player)
		while not self.timer.almostExpired():
			self.ALPHA = - sys.maxsize - 1
			self.BETA = sys.maxsize

			if potentialActions.__len__() == 0:
				break

			for action in potentialActions:
				if self.timer.almostExpired():
					break
				child = self.scg.generateSuccessor(board, action, player)
				self.ALPHA = max(self.ALPHA, self.alphaBeta(child, 1, False))
				if self.ALPHA > maximum:
					# Update move ordering to put this action at the head of the list
					potentialActions.remove(action)
					potentialActions.insert(0,action)
					#potentialActions = self.moveToFront(potentialActions, action)

					maximum = self.ALPHA
					move = action
			if self.timer.almostExpired():
				break
			if self.moveCount < 9:
				break

			searchDepth = self.DEPTH
			self.DEPTH += 1
			if self.DEPTH > self.ABSOLUTEDEPTH:
				break

		self.moveCount += 1
		#if potentialActions.__len__() == 0:
			#print("No possible moves from this state, player loses.")

		self.cacheHits = 0
		self.ties.clear()
		#print("Alpha-Beta result: [" + str(ALPHA) + "," + str(BETA) + "]")
		#print("Got to depth: " + str(searchDepth))
		return move

	def alphaBeta(self, board:Board, searchDepth, maxNode):
		# Terminal nodes in search tree or at max depth we evaluate the board
		if searchDepth == self.DEPTH or self.timer.almostExpired():
			hash = board.hashCode()
			if hash in self.transitionTable:
				bucket = self.transitionTable.get(hash)
				for collision in bucket:
					if board.getBoard() == collision:
						self.cacheHits += 1
						return collision.getHeuristicValue()
				value = self.evaluator.evaluate(board, self.ourPlayer)
				board.setHeuristicValue(value)
				bucket.append(board)
				self.tableSize += 1
				return value

			value = self.evaluator.evaluate(board, self.ourPlayer)
			board.setHeuristicValue(value)
			bucket = [board]
			self.transitionTable[board.hashCode()] = bucket
			self.tableSize += 1
			return value

		if maxNode:
			potentialActions = self.scg.getRelevantActions(board, self.ourPlayer)
			if potentialActions.__len__() == 0:
				return -sys.maxsize - 1
			for action in potentialActions:
				child = self.scg.generateSuccessor(action, self.ourPlayer)
				result = self.alphaBeta(child, searchDepth+1, False)
				if self.timer.almostExpired():
					return max(self.ALPHA, result)
				if result >= self.BETA:
					return result

				self.ALPHA = max(self.ALPHA, result)
			return self.ALPHA
		else:
			potentialActions = self.scg.getRelevantActions(board, self.opponent)
			if potentialActions.__len__() == 0:
				return sys.maxsize
			for action in potentialActions:
				child = self.scg.generateSuccessor(action, self.opponent)
				result = self.alphaBeta(child, searchDepth+1, True)
				if self.timer.almostExpired():
					return min(self.BETA, result)
				if result <= self.ALPHA:
					return result

				self.BETA = min(self.BETA, result)
			return self.BETA


