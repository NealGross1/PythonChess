import numpy as np

class ChessPiece:
    def __init__(self, boardPosition, color):
        self.boardPosition = boardPosition
        self.color = color

    def getPossibleMoves(self,ChessBoard):
        return []

class Pawn(ChessPiece):
    def getPossibleMoves(self, ChessBoard):
        possibleMoves = []
        currPosition = self.boardPosition
        currColor = self.color

        if not(currColor =='black' or currColor =='white') :
            print ('invalid color was for target pawn:'+self.color)
            return None

        for row in range(8):
            for col in range(8):
                tarPosition = [row,col]
                if currColor =='black':
                    #black pawns must move down exactly 1 row
                    if row == currPosition[0] - 1:
                        piecePropertiesAtPosition = ChessBoard.ChessPiecePropertiesAtPosition(row,col)
                        #nothing blocking path
                        if piecePropertiesAtPosition[0] == 0:
                            possibleMoves.append(tarPosition)
                        #enemy to kill diagonally
                        if piecePropertiesAtPosition[0] == 1 and (col == currPosition[1]+1 or col == currPosition[1]-1) and piecePropertiesAtPosition[1]== 'white':
                            possibleMoves.append(tarPosition)

                else currColor == 'white '
                    #white pawns must move up exactly 1 row
                    if row == currPosition[0] + 1:
                        piecePropertiesAtPosition = ChessBoard.ChessPiecePropertiesAtPosition(row,col)
                        #nothing blocking path
                        if piecePropertiesAtPosition[0] == 0:
                            possibleMoves.append(tarPosition)
                        #enemy to kill diagonally
                        if piecePropertiesAtPosition[0] == 1 and (col == currPosition[1]+1 or col == currPosition[1]-1) and piecePropertiesAtPosition[1]== 'black':
                            possibleMoves.append(tarPosition)

        return possibleMoves

class Knight(ChessPiece):
    def getPossibleMoves(self, ChessBoard):
        possibleMoves = []
        currPosition = self.boardPosition
        currColor = self.color

        if not(currColor =='black' or currColor =='white') :
            print ('invalid color was for target Knight:'+self.color)
            return None

        for row in range(8):
            for col in range(8):
                tarPosition = [row,col]
                #knight move in L shape hitting a max of 8 Positions
                if (row == currPosition[0] + 2 or row == currPosition[0] - 2) and (col == currPosition[1] + 1 or col == currPosition[1] - 1):
                    piecePropertiesAtPosition = ChessBoard.ChessPiecePropertiesAtPosition(row,col)
                    if piecePropertiesAtPosition[0] == 0 or (piecePropertiesAtPosition[1]!=currColor):
                        possibleMoves.append(tarPosition)
                if (row == currPosition[0] + 1 or row == currPosition[0] - 1)and (col == currPosition[1] + 2 or col == currPosition[1] - 2):
                    piecePropertiesAtPosition = ChessBoard.ChessPiecePropertiesAtPosition(row,col)
                    if piecePropertiesAtPosition[0] == 0 or (piecePropertiesAtPosition[1]!=currColor):
                        possibleMoves.append(tarPosition)

        return possibleMoves

class King(ChessPiece):
    def getPossibleMoves(self, ChessBoard):
        possibleMoves = []
        currPosition = self.boardPosition
        currColor = self.color

        if not(currColor =='black' or currColor =='white') :
            print ('invalid color was for target King:'+self.color)
            return None

        for row in range(8):
            for col in range(8):
                tarPosition = [row,col]
                #Kings can move in any direction, but limited to one space. Check and check mate is checked seperately
                if ((row == currPosition[0] + 1 or row == currPosition[0] - 1 or row == currPosition[0])
                    and (col == currPosition[1] + 1 or col == currPosition[1] - 1 or col == currPosition[1])
                    and tarPosition != currPosition):
                        piecePropertiesAtPosition = ChessBoard.ChessPiecePropertiesAtPosition(row,col)
                        if piecePropertiesAtPosition[0] == 0 or (piecePropertiesAtPosition[1]!=currColor):
                            possibleMoves.append(tarPosition)

        return possibleMoves

class Bishop(ChessPiece):
    def getPossibleMoves(self, ChessBoard):
        possibleMoves = []
        currPosition = self.boardPosition
        currColor = self.color

        if not(currColor =='black' or currColor =='white') :
            print ('invalid color was for target Bishop:'+self.color)
            return None

        for row in range(8):
            for col in range(8):
                tarPosition = [row,col]
                #Bisops move diagonally xMove == yMove
                if (abs(tarPosition[0] - curPosition[0]) == abs(tarPosition[1] - curPosition[1])) and tarPosition != currPosition:
                    piecePropertiesAtPosition = ChessBoard.ChessPiecePropertiesAtPosition(row,col)
                    if (piecePropertiesAtPosition[0] == 0 or piecePropertiesAtPosition[1]!=currColor) and clearPathToMoveToPosition(ChessBoard, currPosition,tarPosition):
                        possibleMoves.append(tarPosition)

        return possibleMoves

class Queen(ChessPiece):
    def getPossibleMoves(self, ChessBoard):
                possibleMoves = []
                currPosition = self.boardPosition
                currColor = self.color

                if not(currColor =='black' or currColor =='white') :
                    print ('invalid color was for target Queen:'+self.color)
                    return None

                for row in range(8):
                    for col in range(8):
                        tarPosition = [row,col]
                        #Quens can move in the 4 dialgonal directions
                        if (abs(tarPosition[0] - curPosition[0]) == abs(tarPosition[1] - curPosition[1])) and tarPosition != currPosition:
                            piecePropertiesAtPosition = ChessBoard.ChessPiecePropertiesAtPosition(row,col)
                            if (piecePropertiesAtPosition[0] == 0 or piecePropertiesAtPosition[1]!=currColor) and clearPathToMoveToPosition(ChessBoard, currPosition,tarPosition):
                                possibleMoves.append(tarPosition)

                        #Queens can move up down left and right
                        if (((tarPosition[0] == curPosition[0] and tarPosition[1] != curPosition[1])
                            or (tarPosition[0] != curPosition[0] and tarPosition[1] == curPosition[1]))
                            and tarPosition != currPosition):
                
                            piecePropertiesAtPosition = ChessBoard.ChessPiecePropertiesAtPosition(row,col)
                            if (piecePropertiesAtPosition[0] == 0 or piecePropertiesAtPosition[1]!=currColor) and clearPathToMoveToPosition(ChessBoard, currPosition,tarPosition):
                                possibleMoves.append(tarPosition)

                return possibleMoves

class Rook(ChessPiece):
    def getPossibleMoves(self, ChessBoard):
                possibleMoves = []
                currPosition = self.boardPosition
                currColor = self.color

                if not(currColor =='black' or currColor =='white') :
                    print ('invalid color was for target Rook:'+self.color)
                    return None

                for row in range(8):
                    for col in range(8):
                        tarPosition = [row,col]
                        #Rooks move up down left and right
                        if (((tarPosition[0] == curPosition[0] and tarPosition[1] != curPosition[1])
                            or (tarPosition[0] != curPosition[0] and tarPosition[1] == curPosition[1]))
                            and tarPosition != currPosition):

                            piecePropertiesAtPosition = ChessBoard.ChessPiecePropertiesAtPosition(row,col)
                            if (piecePropertiesAtPosition[0] == 0 or piecePropertiesAtPosition[1]!=currColor) and clearPathToMoveToPosition(ChessBoard, currPosition,tarPosition):
                                possibleMoves.append(tarPosition)

                return possibleMoves

class ChessBoard:
    def __init__ (self):
        wp1 = Pawn([1,0],'white')
        wp2 = Pawn([1,1],'white')
        wp3 = Pawn([1,2],'white')
        wp4 = Pawn([1,3],'white')
        wp5 = Pawn([1,4],'white')
        wp6 = Pawn([1,5],'white')
        wp7 = Pawn([1,6],'white')
        wp8 = Pawn([1,7],'white')
        wr1 = Rook([0,0],'white')
        wr2 = Rook([0,7],'white')
        wb1 = Bishop([0,2],'white')
        wb2 = Bishop([0,5],'white')
        wk1 = Knight([0,1],'white')
        wk2 = Knight([0,6],'white')
        wking = King([0,4],'white')
        wqueen = Queen([0,3],'white')

        bp1 = Pawn([6,0],'black')
        bp2 = Pawn([6,1],'black')
        bp3 = Pawn([6,2],'black')
        bp4 = Pawn([6,3],'black')
        bp5 = Pawn([6,4],'black')
        bp6 = Pawn([6,5],'black')
        bp7 = Pawn([6,6],'black')
        bp8 = Pawn([6,7],'black')
        wr1 = Rook([7,0],'black')
        wr2 = Rook([7,7],'black')
        wb1 = Bishop([7,2],'black')
        wb2 = Bishop([7,5],'black')
        wk1 = Knight([7,1],'black')
        wk2 = Knight([7,6],'black')
        wking = King([7,4],'black')
        wQueen = Queen([7,3],'black')
        self.boardSpaces = [[wr1,wk1,wb1,wqueen,wking,wb2,wk2,wr2],
                            [wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8],
                            np.zeros((8,),dtype=int),
                            np.zeros((8,),dtype=int),
                            np.zeros((8,),dtype=int),
                            np.zeros((8,),dtype=int),
                            [bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8],
                            [br1,bk1,bb1,bqueen,bking,bb2,bk2,br2]]
        self.history = [[wr1,wk1,wb1,wqueen,wking,wb2,wk2,wr2],
                            [wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8],
                            np.zeros((8,),dtype=int),
                            np.zeros((8,),dtype=int),
                            np.zeros((8,),dtype=int),
                            np.zeros((8,),dtype=int),
                            [bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8],
                            [br1,bk1,bb1,bqueen,bking,bb2,bk2,br2]]

    def allValidMoves (self):
        #compile a list of each piece that can move and what position
        # potentially a starting_position with a list of ending positions
        return None

    def movePiece(self, startingPiecePosition, endingPiecePosition):
        #move the chess piece at starting Position to ending Position removing any taken piecePropertiesAtPosition
        #TODO castling moves
        return None

    def _addPiece(self, chesspiece, Position = None):
        if Position == None:
            Position= chesspiece.boardPosition
        #TODO add piece to board

    def _removePiece(self, chesspiece):
        currPosition = chesspiece.boardPosition
        #TODO remove piece from board

    def isCheck(self):
        #TODO evaluate the current state of the board for Check condiitions
        return False

    def isCheckMate(self):
        #TODO evaluate the current state of the board for Check Mate condiitions
        return False

    def _addHistory(self):
        #store the current state of the board into history
        return None

    def ChessPiecePropertiesAtPosition (self, position):
    #returns [pieceAtLocatin(0 no piece or 1 for existence), piece color as string ]
        #TODO look up better way to get objects out of nested lists
        row = self.boardSpaces[position[0]]
        chessPiece = row[position[1]]
        if chessPiece != 0 :
            return 1, chessPiece.color
        else
            return 0, None

    def _clearPathToMoveToPositionGivenDirection(self, startPosition, endPosition, xMove,yMove):
        #max 7 moves
        for step in range(1,8):
            tarPosition[0] = startPosition[0]+ (step*xMove)
            tarPosition[1] = startPosition[1]+ (step*xMove)
            if tarPosition == endPosition:
                return True
            pieceExists, pieceColor = ChessPiecePropertiesAtPosition(self, tarPosition)
            if pieceExists:
                return False


    def clearPathToMoveToPosition(self, startPosition, endPosition):
    #returns true if path is clear of other pieces otherwise returns False
        xMovement = endPosition[1] - startPostion[1]
        yMovement = endPosition[0] - startPosition[0]
        return _clearPathToMoveToPositionGivenDirection(self, startPosition endPosition,_normalizeDirections(xMovement),_normalizeDirections(yMovement) )







def _normalizeDirections(directionMagnitude):
#takes any magnitude of direction and normalizes it to 1 , -1, or 0
    if directionMagnitude>0 :
        return 1
    elif directionMagnitude == 0:
        return 0
    else
        return -1