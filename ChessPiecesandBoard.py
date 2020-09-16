import numpy as np


class ChessPiece:
    def __init__(self, boardPosition, color):
        self.boardPosition = boardPosition
        self.color = color
        self.hasMoved = False

    def getPossibleMoves(self, ChessBoard):
        return []
    
    
    
class Pawn(ChessPiece):
    def getPossibleMoves(self, ChessBoard):
        possibleMoves = []
        possibleMovements = []
        possibleKillMoves =[]
        currPosition = self.boardPosition
        currColor = self.color

        if not(currColor == 'black' or currColor == 'white'):
            print('invalid color was given for target pawn:'+self.color)
            return None

        if currColor == 'black':
            movementDirection = 1
        else:
            movementDirection = -1
        
        if currPosition[1] - 1 >= 0 and currPosition[1] + 1 <= 7  and currPosition[0]+ movementDirection >= 0 and currPosition[0]+ movementDirection <= 7: 
            possibleKillMoves =[[currPosition[0]+ movementDirection, currPosition[1] + 1], [currPosition[0]+ movementDirection, currPosition[1] - 1]] 
        elif currPosition[1] + 1 <= 6  and currPosition[0]+ movementDirection >= 0 and currPosition[0]+ movementDirection <= 7:
            possibleKillMoves =[ [currPosition[0]+ movementDirection, currPosition[1] + 1]] 
        elif currPosition[1] - 1 > 0 and currPosition[0]+ movementDirection >= 0 and currPosition[0]+ movementDirection <= 7: 
            possibleKillMoves =[[currPosition[0]+ movementDirection, currPosition[1] - 1]]
        else: 
            possibleKillMoves =[]

        if self.hasMoved and currPosition[0]+ movementDirection >= 0 and currPosition[0]+ movementDirection <= 7:
            possibleMovements = [[currPosition[0] + movementDirection, currPosition[1]]]
        elif currPosition[0]+ movementDirection >= 0 and currPosition[0]+ movementDirection <= 7:
            possibleMovements = [[currPosition[0] + movementDirection, currPosition[1]],  [currPosition[0]+ 2*movementDirection, currPosition[1]]]
        else:
            possibleMovements = []

        for tarPosition in possibleKillMoves:  
            piecePropertiesAtPosition = ChessBoard.chessPiecePropertiesAtPosition([tarPosition[0], tarPosition[1]])    
            # enemy to kill diagonally
            if piecePropertiesAtPosition[0] and piecePropertiesAtPosition[1] != currColor:
                possibleMoves.append(tarPosition)

        for tarPosition in possibleMovements:
            #if tarPosition[0] + movementDirection < 7 and tarPosition[0] + movementDirection >= 0:
            if ChessBoard.clearPathToMoveToPosition(currPosition, [tarPosition[0] + movementDirection, tarPosition[1]]):
                possibleMoves.append(tarPosition)

        return possibleMoves

    def copyPiece(self):
        copiedPawn = Pawn(self.boardPosition,self.color)
        copiedPawn.hasMoved = self.hasMoved
        return copiedPawn

class Knight(ChessPiece):
    def getPossibleMoves(self, ChessBoard):
        possibleMoves = []
        currPosition = self.boardPosition
        currColor = self.color

        if not(currColor == 'black' or currColor == 'white'):
            print('invalid color was for target Knight:'+self.color)
            return None

        for row in range(8):
            for col in range(8):
                tarPosition = [row, col]
                # knight move in L shape hitting a max of 8 Positions
                if (row == currPosition[0] + 2 or row == currPosition[0] - 2) and (col == currPosition[1] + 1 or col == currPosition[1] - 1):
                    piecePropertiesAtPosition = ChessBoard.chessPiecePropertiesAtPosition([
                                                                                          row, col])
                    if piecePropertiesAtPosition[0] == 0 or (piecePropertiesAtPosition[1] != currColor):
                        possibleMoves.append(tarPosition)
                if (row == currPosition[0] + 1 or row == currPosition[0] - 1) and (col == currPosition[1] + 2 or col == currPosition[1] - 2):
                    piecePropertiesAtPosition = ChessBoard.chessPiecePropertiesAtPosition([
                                                                                          row, col])
                    if piecePropertiesAtPosition[0] == 0 or (piecePropertiesAtPosition[1] != currColor):
                        possibleMoves.append(tarPosition)

        return possibleMoves

    def copyPiece(self):
        copiedKnight = Knight(self.boardPosition,self.color)
        return copiedKnight

class King(ChessPiece):
    def getPossibleMoves(self, ChessBoard):
        possibleMoves = []
        currPosition = self.boardPosition
        currColor = self.color

        if not(currColor == 'black' or currColor == 'white'):
            print('invalid color was for target King:'+self.color)
            return None

        for row in range(8):
            for col in range(8):
                tarPosition = [row, col]
                # Kings can move in any direction, but limited to one space. Check and check mate is checked seperately
                if ((row == currPosition[0] + 1 or row == currPosition[0] - 1 or row == currPosition[0])
                    and (col == currPosition[1] + 1 or col == currPosition[1] - 1 or col == currPosition[1])
                        and tarPosition != currPosition):
                    piecePropertiesAtPosition = ChessBoard.chessPiecePropertiesAtPosition([
                                                                                          row, col])
                    if piecePropertiesAtPosition[0] == 0 or (piecePropertiesAtPosition[1] != currColor):
                        possibleMoves.append(tarPosition)

        return possibleMoves

    def copyPiece(self):
        copiedKing = King(self.boardPosition,self.color)
        copiedKing.hasMoved = self.hasMoved
        return copiedKing

class Bishop(ChessPiece):
    def getPossibleMoves(self, ChessBoard):
        possibleMoves = []
        currPosition = self.boardPosition
        currColor = self.color

        if not(currColor == 'black' or currColor == 'white'):
            print('invalid color was for target Bishop:'+self.color)
            return None

        for row in range(8):
            for col in range(8):
                tarPosition = [row, col]
                # Bisops move diagonally xMove == yMove
                if (abs(tarPosition[0] - currPosition[0]) == abs(tarPosition[1] - currPosition[1])) and tarPosition != currPosition:
                    piecePropertiesAtPosition = ChessBoard.chessPiecePropertiesAtPosition([
                                                                                          row, col])
                    if (piecePropertiesAtPosition[0] == 0 or piecePropertiesAtPosition[1] != currColor) and ChessBoard.clearPathToMoveToPosition(currPosition, tarPosition):
                        possibleMoves.append(tarPosition)

        return possibleMoves
    
    def copyPiece(self):
            copiedBishop = Bishop(self.boardPosition,self.color)
            return copiedBishop

class Queen(ChessPiece):
    def getPossibleMoves(self, ChessBoard):
        possibleMoves = []
        currPosition = self.boardPosition
        currColor = self.color

        if not(currColor == 'black' or currColor == 'white'):
            print('invalid color was for target Queen:'+self.color)
            return None

        for row in range(8):
            for col in range(8):
                tarPosition = [row, col]
                # Quens can move in the 4 dialgonal directions
                if (abs(tarPosition[0] - currPosition[0]) == abs(tarPosition[1] - currPosition[1])) and tarPosition != currPosition:
                    piecePropertiesAtPosition = ChessBoard.chessPiecePropertiesAtPosition([
                                                                                          row, col])
                    if (piecePropertiesAtPosition[0] == 0 or piecePropertiesAtPosition[1] != currColor) and ChessBoard.clearPathToMoveToPosition(currPosition, tarPosition):
                        possibleMoves.append(tarPosition)

                # Queens can move up down left and right
                if (((tarPosition[0] == currPosition[0] and tarPosition[1] != currPosition[1])
                     or (tarPosition[0] != currPosition[0] and tarPosition[1] == currPosition[1]))
                        and tarPosition != currPosition):

                    piecePropertiesAtPosition = ChessBoard.chessPiecePropertiesAtPosition([
                                                                                          row, col])
                    if (piecePropertiesAtPosition[0] == 0 or piecePropertiesAtPosition[1] != currColor) and ChessBoard.clearPathToMoveToPosition(currPosition, tarPosition):
                        possibleMoves.append(tarPosition)

        return possibleMoves

    def copyPiece(self):
            copiedQueen = Queen(self.boardPosition,self.color)
            return copiedQueen

class Rook(ChessPiece):
    def getPossibleMoves(self, ChessBoard):
        possibleMoves = []
        currPosition = self.boardPosition
        currColor = self.color

        if not(currColor == 'black' or currColor == 'white'):
            print('invalid color was for target Rook:'+self.color)
            return None

        for row in range(8):
            for col in range(8):
                tarPosition = [row, col]
                # Rooks move up down left and right
                if (((tarPosition[0] == currPosition[0] and tarPosition[1] != currPosition[1])
                     or (tarPosition[0] != currPosition[0] and tarPosition[1] == currPosition[1]))
                        and tarPosition != currPosition):

                    piecePropertiesAtPosition = ChessBoard.chessPiecePropertiesAtPosition([
                                                                                          row, col])
                    if (piecePropertiesAtPosition[0] == 0 or piecePropertiesAtPosition[1] != currColor) and ChessBoard.clearPathToMoveToPosition(currPosition, tarPosition):
                        possibleMoves.append(tarPosition)

        return possibleMoves

    def copyPiece(self):
        copiedRook = Rook(self.boardPosition,self.color)
        return copiedRook

class ChessBoard:
    def __init__(self):
        bp1 = Pawn([1, 0], 'black')
        bp2 = Pawn([1, 1], 'black')
        bp3 = Pawn([1, 2], 'black')
        bp4 = Pawn([1, 3], 'black')
        bp5 = Pawn([1, 4], 'black')
        bp6 = Pawn([1, 5], 'black')
        bp7 = Pawn([1, 6], 'black')
        bp8 = Pawn([1, 7], 'black')
        br1 = Rook([0, 0], 'black')
        br2 = Rook([0, 7], 'black')
        bb1 = Bishop([0, 2], 'black')
        bb2 = Bishop([0, 5], 'black')
        bk1 = Knight([0, 1], 'black')
        bk2 = Knight([0, 6], 'black')
        bking = King([0, 4], 'black')
        bqueen = Queen([0, 3], 'black')

        wp1 = Pawn([6, 0], 'white')
        wp2 = Pawn([6, 1], 'white')
        wp3 = Pawn([6, 2], 'white')
        wp4 = Pawn([6, 3], 'white')
        wp5 = Pawn([6, 4], 'white')
        wp6 = Pawn([6, 5], 'white')
        wp7 = Pawn([6, 6], 'white')
        wp8 = Pawn([6, 7], 'white')
        wr1 = Rook([7, 0], 'white')
        wr2 = Rook([7, 7], 'white')
        wb1 = Bishop([7, 2], 'white')
        wb2 = Bishop([7, 5], 'white')
        wk1 = Knight([7, 1], 'white')
        wk2 = Knight([7, 6], 'white')
        wking = King([7, 4], 'white')
        wqueen = Queen([7, 3], 'white')
        self.boardSpaces = [[br1, bk1, bb1, bqueen, bking, bb2, bk2, br2],
                            [bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0],
                            [wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8],
                            [wr1, wk1, wb1, wqueen, wking, wb2, wk2, wr2]]
        self.history = self.boardSpaces

    def allValidMoves(self, color):
        # as long as the move is a possible move and does not cause check, or takes the player out of check, its a valid move
        validMoves = []
        possibleMoves = self.getPossibleMoves(color)
        for i in range(len(possibleMoves)):
            validPieceMoves = []
            for j in range(len(possibleMoves[i][1])):
                causesCheck = self.movePutsPlayerIntoCheck(
                    possibleMoves[i][0].boardPosition, possibleMoves[i][1][j])
                if causesCheck == False:
                    validPieceMoves.append(possibleMoves[i][1][j])
            validMoves.append([possibleMoves[i][0], validPieceMoves])

        return validMoves

    def getPossibleMoves(self, color):
        allMoves = []
        for row in range(8):
            for col in range(8):
                isPiece, tarColor = self.chessPiecePropertiesAtPosition([
                                                                        row, col])
                if isPiece and tarColor == color:
                    tarPiece = self.getPieceAtPosition([row, col])
                    possibleMoves = tarPiece.getPossibleMoves(self)
                    allMoves.append([tarPiece, possibleMoves])
        return allMoves

    def movePutsPlayerIntoCheck(self, color, startPosition, endPosition):
        copiedBoard = self.copyBoard()
        copiedBoard.movePiece(startPosition, endPosition)
        isInCheck = copiedBoard.isCheck(color)
        copiedBoard.destructor()
        return isInCheck

    def copyBoard(self):
        newBoard = ChessBoard()
        newBoard.clearBoard()
        for row in range(8):
            for col in range(8):
                tar = self.getPieceAtPosition([row, col])
                if not type(tar) == int:
                    copiedTarget = tar.copyPiece()
                    newBoard.boardSpaces[row][col] = copiedTarget

        return newBoard

    def getPieceAtPosition(self, position):
        return self.boardSpaces[position[0]][position[1]]

    def getPieceAtPositionAsText(self, position):
        if type(self.boardSpaces[position[0]][position[1]]) is Pawn and self.boardSpaces[position[0]][position[1]].color == "white":
            return "wP"
        if type(self.boardSpaces[position[0]][position[1]]) is Pawn and self.boardSpaces[position[0]][position[1]].color == "black":
            return "bP"
        if type(self.boardSpaces[position[0]][position[1]]) is Rook and self.boardSpaces[position[0]][position[1]].color == "white":
            return "wR"
        if type(self.boardSpaces[position[0]][position[1]]) is Rook and self.boardSpaces[position[0]][position[1]].color == "black":
            return "bR"
        if type(self.boardSpaces[position[0]][position[1]]) is Knight and self.boardSpaces[position[0]][position[1]].color == "white":
            return "wT"
        if type(self.boardSpaces[position[0]][position[1]]) is Knight and self.boardSpaces[position[0]][position[1]].color == "black":
            return "bT"
        if type(self.boardSpaces[position[0]][position[1]]) is Bishop and self.boardSpaces[position[0]][position[1]].color == "white":
            return "wB"
        if type(self.boardSpaces[position[0]][position[1]]) is Bishop and self.boardSpaces[position[0]][position[1]].color == "black":
            return "bB"
        if type(self.boardSpaces[position[0]][position[1]]) is Queen and self.boardSpaces[position[0]][position[1]].color == "white":
            return "wQ"
        if type(self.boardSpaces[position[0]][position[1]]) is Queen and self.boardSpaces[position[0]][position[1]].color == "black":
            return "bQ"
        if type(self.boardSpaces[position[0]][position[1]]) is King and self.boardSpaces[position[0]][position[1]].color == "white":
            return "wK"
        if type(self.boardSpaces[position[0]][position[1]]) is King and self.boardSpaces[position[0]][position[1]].color == "black":
            return "bK"
        return "e"

    def movePiece(self, startingPiecePosition, endingPiecePosition):
        # move the chess piece at starting Position to ending Position removing any taken piecePropertiesAtPosition
        endPiece = self.getPieceAtPosition(endingPiecePosition)
        startPiece = self.getPieceAtPosition(startingPiecePosition)
        if endPiece != 0:
            self._removePiece(endPiece, deletePiece=True)
        self._removePiece(startPiece)
        self._addPiece(startPiece, list(endingPiecePosition))
        startPiece.hasMoved = True
        # TODO castling moves

    def _addPiece(self, chesspiece, position=None):
        if type(chesspiece) == int:
            return chesspiece

        if position == None:
            position = list(chesspiece.boardPosition)

        
        currBoard = self.boardSpaces
        positionProperties = self.chessPiecePropertiesAtPosition(position)
        if positionProperties[0]:
            print('You must remove the current piece before adding a piece')
            return False
        else:
            self.boardSpaces[position[0]][position[1]] = chesspiece
            if chesspiece.boardPosition != position:
                chesspiece.boardPosition = list(position)
            return True

    def _removePiece(self, chesspiece, currPosition=None, deletePiece=False):
        if type(chesspiece) == int:
            return 
        if currPosition == None:
            currPosition = chesspiece.boardPosition
        self.boardSpaces[currPosition[0]][currPosition[1]] = 0
        if deletePiece:
            del chesspiece

    def isCheck(self, color):
        # find king of given color and if it's position is in the possible moves of opposite color then check
        isCheck = False
        found = False
        for row in range(8):
            for col in range(8):
                tarKing = self.getPieceAtPosition([row, col])
                if isinstance(tarKing,King):
                    if tarKing.color == color:
                        found = True
                if found:
                    break
            if found:
                break 

        if color == 'white':
            possibleEnemyMoves = self.getPossibleMoves('black')
        else:
            possibleEnemyMoves = self.getPossibleMoves('white')

        for i in range(len(possibleEnemyMoves)):
            if tarKing.boardPosition in possibleEnemyMoves[i][1]:
                return True

        return isCheck
    
    def movesToGetOutofCheck (self, color):
        movesOutOfCheck = []
        if color == 'white':
            possibleMoves = self.getPossibleMoves('white')
        else:
            possibleMoves = self.getPossibleMoves('black')

        for moves in possibleMoves:
            startLocation = moves[0].boardPosition
            if len(moves[1]) > 0:
                for endLocation in moves[1]:
                    if not (endLocation in movesOutOfCheck):
                        isCheck = self.movePutsPlayerIntoCheck(color, startLocation, endLocation)
                        #print ('isCheck:', isCheck)
                        #print('selected piece:', moves[0], ' @ ', startLocation)
                        #print('moving to:', endLocation)
                        if not(isCheck):
                            movesOutOfCheck.append(endLocation)

        return movesOutOfCheck


    def _addHistory(self):
        # store the current state of the board into history
        return None

    def chessPiecePropertiesAtPosition(self, position):
        # returns [pieceAtLocatin(0 no piece or 1 for existence), piece color as string ]
        # TODO look up better way to get objects out of nested lists
        try:
            row = self.boardSpaces[position[0]]
            chessPiece = row[position[1]]
            if chessPiece != 0:
                return 1, chessPiece.color
            else:
                return 0, None
        
        except ValueError:
            return 0, None

    def _clearPathToMoveToPositionGivenDirection(self, startPosition, endPosition, xMove, yMove):
        # max 7 moves
        tarPosition = [-1, -1]
        for step in range(1, 8):
            tarPosition[0] = startPosition[0] + (step*yMove)
            tarPosition[1] = startPosition[1] + (step*xMove)
            if tarPosition == endPosition:
                return True
            pieceExists, pieceColor = self.chessPiecePropertiesAtPosition(
                tarPosition)
            if pieceExists:
                return False

    def clearPathToMoveToPosition(self, startPosition, endPosition):
        # returns true if path is clear of other pieces otherwise returns False
        xMovement = endPosition[1] - startPosition[1]
        yMovement = endPosition[0] - startPosition[0]
        return self._clearPathToMoveToPositionGivenDirection(startPosition, endPosition, _normalizeDirections(xMovement), _normalizeDirections(yMovement))

    def clearBoard(self):
        for row in range(8):
            for col in range(8):
                tarPiece = self.getPieceAtPosition([row, col])
                if not type(tarPiece) == int:
                    #print ( type(tarPiece))
                    self._removePiece(tarPiece, deletePiece=True)

    def destructor(self):
        for row in range(8):
            for col in range(8):
                tarPiece = self.getPieceAtPosition([row, col])
                if tarPiece != 0:
                    del tarPiece
        del self


def _normalizeDirections(directionMagnitude):
    # takes any magnitude of direction and normalizes it to 1 , -1, or 0
    if directionMagnitude > 0:
        return 1
    elif directionMagnitude == 0:
        return 0
    else:
        return -1


def getBoardDescription(self):
    boardDescription = [
     ['e','e','e','e','e','e','e','e'],
     ['e','e','e','e','e','e','e','e'],
     ['e','e','e','e','e','e','e','e'],
     ['e','e','e','e','e','e','e','e'],
     ['e','e','e','e','e','e','e','e'], 
     ['e','e','e','e','e','e','e','e'], 
     ['e','e','e','e','e','e','e','e'], 
     ['e','e','e','e','e','e','e','e']]
    for row in range(8):
        for col in range(8):
            piece = self.getPieceAtPositionAsText([row, col])
            boardDescription[row][col] = piece
    return boardDescription
