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
        #TODO double pawn step when pawn has not moved yet
        for row in range(8):
            for col in range(8):
                tarPosition = [row,col]
                if currColor =='black':
                    movementDirection = -1
                else:
                    movementDirection = 1
                if row == currPosition[0] + movementDirection :
                    piecePropertiesAtPosition = ChessBoard.chessPiecePropertiesAtPosition([row,col])
                    #nothing blocking path
                    if piecePropertiesAtPosition[0] == 0 and col == currPosition[1]:
                        possibleMoves.append(tarPosition)
                    #enemy to kill diagonally
                    if piecePropertiesAtPosition[0] == 1 and (col == currPosition[1]+1 or col == currPosition[1]-1) and piecePropertiesAtPosition[1] != currColor:
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
                    piecePropertiesAtPosition = ChessBoard.chessPiecePropertiesAtPosition([row,col])
                    if piecePropertiesAtPosition[0] == 0 or (piecePropertiesAtPosition[1]!=currColor):
                        possibleMoves.append(tarPosition)
                if (row == currPosition[0] + 1 or row == currPosition[0] - 1)and (col == currPosition[1] + 2 or col == currPosition[1] - 2):
                    piecePropertiesAtPosition = ChessBoard.chessPiecePropertiesAtPosition([row,col])
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
                        piecePropertiesAtPosition = ChessBoard.chessPiecePropertiesAtPosition([row,col])
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
                if (abs(tarPosition[0] - currPosition[0]) == abs(tarPosition[1] - currPosition[1])) and tarPosition != currPosition:
                    piecePropertiesAtPosition = ChessBoard.chessPiecePropertiesAtPosition([row,col])
                    if (piecePropertiesAtPosition[0] == 0 or piecePropertiesAtPosition[1]!=currColor) and ChessBoard.clearPathToMoveToPosition(currPosition,tarPosition):
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
                        if (abs(tarPosition[0] - currPosition[0]) == abs(tarPosition[1] - currPosition[1])) and tarPosition != currPosition:
                            piecePropertiesAtPosition = ChessBoard.chessPiecePropertiesAtPosition([row,col])
                            if (piecePropertiesAtPosition[0] == 0 or piecePropertiesAtPosition[1]!=currColor) and ChessBoard.clearPathToMoveToPosition(currPosition,tarPosition):
                                possibleMoves.append(tarPosition)

                        #Queens can move up down left and right
                        if (((tarPosition[0] == currPosition[0] and tarPosition[1] != currPosition[1])
                            or (tarPosition[0] != currPosition[0] and tarPosition[1] == currPosition[1]))
                            and tarPosition != currPosition):

                            piecePropertiesAtPosition = ChessBoard.chessPiecePropertiesAtPosition([row,col])
                            if (piecePropertiesAtPosition[0] == 0 or piecePropertiesAtPosition[1]!=currColor) and ChessBoard.clearPathToMoveToPosition(currPosition,tarPosition):
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
                        if (((tarPosition[0] == currPosition[0] and tarPosition[1] != currPosition[1])
                            or (tarPosition[0] != currPosition[0] and tarPosition[1] == currPosition[1]))
                            and tarPosition != currPosition):

                            piecePropertiesAtPosition = ChessBoard.chessPiecePropertiesAtPosition([row,col])
                            if (piecePropertiesAtPosition[0] == 0 or piecePropertiesAtPosition[1]!=currColor) and ChessBoard.clearPathToMoveToPosition( currPosition,tarPosition):
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
        br1 = Rook([7,0],'black')
        br2 = Rook([7,7],'black')
        bb1 = Bishop([7,2],'black')
        bb2 = Bishop([7,5],'black')
        bk1 = Knight([7,1],'black')
        bk2 = Knight([7,6],'black')
        bking = King([7,4],'black')
        bqueen = Queen([7,3],'black')
        self.boardSpaces = [[wr1,wk1,wb1,wqueen,wking,wb2,wk2,wr2],
                            [wp1,wp2,wp3,wp4,wp5,wp6,wp7,wp8],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [0,0,0,0,0,0,0,0],
                            [bp1,bp2,bp3,bp4,bp5,bp6,bp7,bp8],
                            [br1,bk1,bb1,bqueen,bking,bb2,bk2,br2]]
        self.history = self.boardSpaces

    def allValidMoves (self):
        #compile a list of each piece that can move and what position
        # potentially a starting_position with a list of ending positions
        return None

    def getPieceAtPosition(self,position):
        return self.boardSpaces[position[0]][position[1]]

    def movePiece(self, startingPiecePosition, endingPiecePosition):
        #move the chess piece at starting Position to ending Position removing any taken piecePropertiesAtPosition
        endPiece = self.getPieceAtPosition(endingPiecePosition)
        startPiece = self.getPieceAtPosition(startingPiecePosition)
        if endPiece != 0 :
            self._removePiece(endPiece, deletePiece=True)
        self._addPiece(startPiece,endingPiecePosition)
        self._removePiece(startPiece)
        startPiece.boardPosition=endingPiecePosition
        #TODO castling moves

    def _addPiece(self, chesspiece, position = None):
        if position == None:
            position= chesspiece.boardPosition

        currBoard = self.boardSpaces
        positionProperties = self.chessPiecePropertiesAtPosition(position)
        if positionProperties[0]:
            print('You must remove the current piece before adding a piece')
            return False
        else:
            self.boardSpaces[position[0]][position[1]]= chesspiece
            if chesspiece.boardPosition != position :
                chesspiece.boardPosition = position
            return True

    def _removePiece(self, chesspiece, currPosition=None, deletePiece = False):
        if currPosition == None :
            currPosition = chesspiece.boardPosition
        self.boardSpaces[currPosition[0]][currPosition[1]]= 0
        if deletePiece :
            del chesspiece

    def isCheck(self):
        #TODO evaluate the current state of the board for Check condiitions
        return False

    def isCheckMate(self):
        #TODO evaluate the current state of the board for Check Mate condiitions
        return False

    def _addHistory(self):
        #store the current state of the board into history
        return None

    def chessPiecePropertiesAtPosition (self, position):
    #returns [pieceAtLocatin(0 no piece or 1 for existence), piece color as string ]
        #TODO look up better way to get objects out of nested lists
        row = self.boardSpaces[position[0]]
        chessPiece = row[position[1]]
        if chessPiece != 0 :
            return 1, chessPiece.color
        else:
            return 0, None

    def _clearPathToMoveToPositionGivenDirection(self, startPosition, endPosition, xMove,yMove):
        #max 7 moves
        tarPosition =[-1,-1]
        for step in range(1,8):
            tarPosition[0] = startPosition[0]+ (step*yMove)
            tarPosition[1] = startPosition[1]+ (step*xMove)
            if tarPosition == endPosition:
                return True
            pieceExists, pieceColor = self.chessPiecePropertiesAtPosition(tarPosition)
            if pieceExists:
                return False


    def clearPathToMoveToPosition(self, startPosition, endPosition):
    #returns true if path is clear of other pieces otherwise returns False
        xMovement = endPosition[1] - startPosition[1]
        yMovement = endPosition[0] - startPosition[0]
        return self._clearPathToMoveToPositionGivenDirection(startPosition, endPosition,_normalizeDirections(xMovement),_normalizeDirections(yMovement) )

    def clearBoard(self):
        for row in range(8):
            for col in range(8):
                tarPiece = self.getPieceAtPosition([row,col])
                if tarPiece != 0:
                    self._removePiece(tarPiece, deletePiece = True)

    def destructor(self):
        for row in range(8):
            for col in range(8):
                tarPiece = self.getPieceAtPosition([row,col])
                if tarPiece != 0 :
                    del tarPiece
        del self




def _normalizeDirections(directionMagnitude):
#takes any magnitude of direction and normalizes it to 1 , -1, or 0
    if directionMagnitude>0 :
        return 1
    elif directionMagnitude == 0:
        return 0
    else:
        return -1
