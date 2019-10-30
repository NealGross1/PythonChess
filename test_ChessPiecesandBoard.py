import unittest
from ChessPiecesandBoard import *

class TestChessPiece(unittest.TestCase):
    def test_init(self):
        newPiece = ChessPiece([0,3],'white')
        self.assertEqual(newPiece.color, 'white')
        self.assertEqual(newPiece.boardPosition,[0,3])

if __name__ == '__main__':
    unittest.main()
