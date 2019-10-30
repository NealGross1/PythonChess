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

        #assert expected empty locations are empty

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
