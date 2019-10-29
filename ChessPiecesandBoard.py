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
                        piecePropertiesAtLocation = ChessBoard.ChessPiecePropertiesAtLocation(row,col)
                        #nothing blocking path
                        if piecePropertiesAtLocation[0] == 0:
                            possibleMoves.append(tarPosition)
                        #enemy to kill diagonally
                        if piecePropertiesAtLocation[0] == 1 and (col == currPosition[1]+1 or col == currPosition[1]-1) and piecePropertiesAtLocation[1]== 'white':
                            possibleMoves.append(tarPosition)

                else currColor == 'white '
                    #white pawns must move up exactly 1 row
                    if row == currPosition[0] + 1:
                        piecePropertiesAtLocation = ChessBoard.ChessPiecePropertiesAtLocation(row,col)
                        #nothing blocking path
                        if piecePropertiesAtLocation[0] == 0:
                            possibleMoves.append(tarPosition)
                        #enemy to kill diagonally
                        if piecePropertiesAtLocation[0] == 1 and (col == currPosition[1]+1 or col == currPosition[1]-1) and piecePropertiesAtLocation[1]== 'black':
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
                #knight move in L shape hitting a max of 8 locations
                if (row == currPosition[0] + 2 or row == currPosition[0] - 2) and (col == currPosition[1] + 1 or col == currPosition[1] - 1):
                    piecePropertiesAtLocation = ChessBoard.ChessPiecePropertiesAtLocation(row,col)
                    if piecePropertiesAtLocation[0] == 0 or (piecePropertiesAtLocation[1]!=currColor):
                        possibleMoves.append(tarPosition)
                if (row == currPosition[0] + 1 or row == currPosition[0] - 1)and (col == currPosition[1] + 2 or col == currPosition[1] - 2):
                    piecePropertiesAtLocation = ChessBoard.ChessPiecePropertiesAtLocation(row,col)
                    if piecePropertiesAtLocation[0] == 0 or (piecePropertiesAtLocation[1]!=currColor):
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
                if (row == currPosition[0] + 1 or row == currPosition[0] - 1 or row == currPosition[0]) and (col == currPosition[1] + 1 or col == currPosition[1] - 1 or col == currPosition[1]):
                    #exclude the possiblity of not moving
                    if row != currPosition[0] and col != currPosition[1]:
                        piecePropertiesAtLocation = ChessBoard.ChessPiecePropertiesAtLocation(row,col)
                        if piecePropertiesAtLocation[0] == 0 or (piecePropertiesAtLocation[1]!=currColor):
                            possibleMoves.append(tarPosition)

        return possibleMoves

class Bishop(ChessPiece):
    def getPossibleMoves(self, ChessBoard):
        return []

class Queen(ChessPiece):
    def getPossibleMoves(self, ChessBoard):
        return []

class Rook(ChessPiece):
    def getPossibleMoves(self, ChessBoard):
        return []

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
