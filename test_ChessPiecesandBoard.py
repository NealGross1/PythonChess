import unittest
from ChessPiecesandBoard import *

class TestChessPiece(unittest.TestCase):
    def test_init(self):
        newPiece = ChessPiece([0,3],'white')
        self.assertEqual(newPiece.color, 'white')
        self.assertEqual(newPiece.boardPosition,[0,3])
        del newPiece

class TestChessBoard(unittest.TestCase):
    def test_init(self):
        newBoard = ChessBoard()
        boardContents = newBoard.boardSpaces
        #assert all chess pieces are in the correct locations
        for col in range(8):
            #row 1 white backline
            expectedClasses=[Rook,Knight,Bishop,Queen,King,Bishop,Knight,Rook]
            boardContentsRow=boardContents[0]
            self.assertIsInstance(boardContentsRow[col],expectedClasses[col])
            self.assertEqual(boardContentsRow[col].color,'white')
            #row 2 white pawns
            boardContentsRow=boardContents[1]
            self.assertIsInstance(boardContentsRow[col],Pawn)
            self.assertEqual(boardContentsRow[col].color,'white')
            #row 7 black pawns
            boardContentsRow=boardContents[6]
            self.assertIsInstance(boardContentsRow[col],Pawn)
            self.assertEqual(boardContentsRow[col].color,'black')
            #row 8 black backline
            boardContentsRow=boardContents[7]
            self.assertIsInstance(boardContentsRow[col],expectedClasses[col])
            self.assertEqual(boardContentsRow[col].color,'black')
            #all others 0
            for row in range(2,6):
                boardContentsRow=boardContents[row]
                self.assertEqual(boardContentsRow[col],0)

        newBoard.destructor()

    def test_getPieceAtPosition(self):
        newBoard = ChessBoard()
        tarPiece = newBoard.getPieceAtPosition([0,0])
        self.assertIsInstance(tarPiece, Rook)
        self.assertEqual(tarPiece.color,'white')
        tarPiece = newBoard.getPieceAtPosition([4,4])
        self.assertEqual(tarPiece,0)
        newBoard.destructor()

    def test__addPiece(self):
        newBoard = ChessBoard()
        newPiece = Pawn([4,4], 'white')
        newBoard._addPiece(newPiece)
        newBoard._addPiece(newPiece, [2,4])
        tarPiece = newBoard.getPieceAtPosition([4,4])
        self.assertIs(tarPiece,newPiece)
        tarPiece = newBoard.getPieceAtPosition([2,4])
        self.assertIs(tarPiece,newPiece)
        self.assertEqual(tarPiece.boardPosition, [2,4])
        newBoard.destructor()

    def test__removePiece(self):
        newBoard = ChessBoard()
        newPiece = Pawn([4,4], 'white')
        newBoard._addPiece(newPiece)
        newBoard._addPiece(newPiece, [2,4])
        newBoard._removePiece(newPiece, currPosition=[4,4])
        tarPiece = newBoard.getPieceAtPosition([4,4])
        self.assertEqual(tarPiece,0)
        tarPiece = newBoard.getPieceAtPosition([2,4])
        self.assertIsInstance(tarPiece, Pawn)
        self.assertEqual(tarPiece.color, 'white')
        newBoard._removePiece(newPiece, deletePiece=True)
        tarPiece = newBoard.getPieceAtPosition([2,4])
        self.assertEqual(tarPiece,0)
        newBoard.destructor()

    def test_chessPiecePropertiesAtPosition(self):
        newBoard = ChessBoard()
        pieceProperties = newBoard.chessPiecePropertiesAtPosition([0,1])
        self.assertEqual(pieceProperties,(1,'white'))
        pieceProperties = newBoard.chessPiecePropertiesAtPosition([4,4])
        self.assertEqual(pieceProperties,(0,None))
        newBoard.destructor()

    def test_clearBoard(self):
        newBoard=ChessBoard()
        newBoard.clearBoard()
        for row in range(8):
            for col in range(8):
                tarPiece = newBoard.getPieceAtPosition([row,col])
                self.assertEqual(tarPiece, 0)

    def test__clearPathToMoveToPositionGivenDirection(self):
        #create board with obstructed paths
        newBoard = ChessBoard()
        newBoard.clearBoard()
        #piece to move
        wQ1 = Queen([4,4],'white')
        #pieces to block
        wQ2 = Queen([1,4],'white')
        wQ3 = Queen([5,4],'white')
        wQ4 = Queen([4,1],'white')
        wQ5 = Queen([4,6],'white')
        wQ6 = Queen([5,5],'white')
        wQ7 = Queen([2,2],'white')
        wQ8 = Queen([2,6],'white')
        wQ9 = Queen([5,3],'white')
        #pieces to take
        bQ1 = Queen([0,4],'black')
        bQ2 = Queen([4,0],'black')
        bQ3 = Queen([7,7],'black')
        bQ4 = Queen([1,7],'black')
        piecesToAdd = [wQ1,wQ2,wQ3,wQ4,wQ5,wQ6,wQ7,wQ8,wQ9,bQ1,bQ2,bQ3,bQ4]
        for i in range(len(piecesToAdd)):
            newBoard._addPiece(piecesToAdd[i])

        #unclear paths for 4 diagonals and 4 Dpad directions
        pathClear = newBoard._clearPathToMoveToPositionGivenDirection([4,4] , [0,4],0,-1)
        self.assertFalse(pathClear)
        pathClear = newBoard._clearPathToMoveToPositionGivenDirection([4,4] , [4,0],-1,0)
        self.assertFalse(pathClear)
        pathClear = newBoard._clearPathToMoveToPositionGivenDirection([4,4] , [7,4],0,1)
        self.assertFalse(pathClear)
        pathClear = newBoard._clearPathToMoveToPositionGivenDirection([4,4] , [4,7],1,0)
        self.assertFalse(pathClear)
        pathClear = newBoard._clearPathToMoveToPositionGivenDirection([4,4] , [7,7], 1,1)
        self.assertFalse(pathClear)
        pathClear = newBoard._clearPathToMoveToPositionGivenDirection([4,4] , [0,0], -1,-1 )
        self.assertFalse(pathClear)
        pathClear = newBoard._clearPathToMoveToPositionGivenDirection([4,4] , [1,7], 1,-1 )
        self.assertFalse(pathClear)
        pathClear = newBoard._clearPathToMoveToPositionGivenDirection([4,4] , [7,1], -1,1 )
        self.assertFalse(pathClear)
        #clear paths for 4 diagonals and 4 Dpad directiosn
        piecesToRemove = [wQ2,wQ3,wQ4,wQ5,wQ6,wQ7,wQ8,wQ9]
        for i in range(len(piecesToRemove)):
            newBoard._removePiece(piecesToRemove[i],deletePiece=True)
        pathClear = newBoard._clearPathToMoveToPositionGivenDirection([4,4] , [0,4],0,-1)
        self.assertTrue(pathClear)
        pathClear = newBoard._clearPathToMoveToPositionGivenDirection([4,4] , [4,0],-1,0)
        self.assertTrue(pathClear)
        pathClear = newBoard._clearPathToMoveToPositionGivenDirection([4,4] , [7,4],0,1)
        self.assertTrue(pathClear)
        pathClear = newBoard._clearPathToMoveToPositionGivenDirection([4,4] , [4,7],1,0)
        self.assertTrue(pathClear)
        pathClear = newBoard._clearPathToMoveToPositionGivenDirection([4,4] , [7,7], 1,1)
        self.assertTrue(pathClear)
        pathClear = newBoard._clearPathToMoveToPositionGivenDirection([4,4] , [0,0], -1,-1 )
        self.assertTrue(pathClear)
        pathClear = newBoard._clearPathToMoveToPositionGivenDirection([4,4] , [1,7], 1,-1 )
        self.assertTrue(pathClear)
        pathClear = newBoard._clearPathToMoveToPositionGivenDirection([4,4] , [7,1], -1,1 )
        self.assertTrue(pathClear)
        newBoard.destructor()

    def test_clearPathToMoveToPosition(self):
        #_clearPathToMoveToPositionGivenDirection already tested for obstruction, need to test directional normalization only
        newBoard = ChessBoard()
        newBoard.clearBoard()
        wQ1 = Queen([4,4],'white')
        newBoard._addPiece(wQ1)
        endPathPoints=[[0,4], [4,4], [7,4], [4,7], [0,0],[7,7],[1,7],[7,1]]
        for i in range(len(endPathPoints)):
            clearPath = newBoard.clearPathToMoveToPosition([4,4],endPathPoints[i])
            self.assertTrue(clearPath)

class TestPawn(unittest.TestCase):
    def test_possibleMoves(self):
        pawnCenterOfBoard = Pawn([4,4], 'white')
        pawnBlackCenterOfBoard = Pawn([2,4],'black')
        #newBoard = ChessBoard()
        #black movement & white movement difference

        #off the board movement

        #diagnal movement with and without a piece there

if __name__ == '__main__':
    unittest.main()
