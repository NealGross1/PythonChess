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
    print("running pawn tests")
    def test_possibleMoves(self):
        pawnCenterOfBoard = Pawn([4,4], 'white')
        pawnBlackInfrontOfPawn = Pawn([2,4],'black')
        pawnBlackInfrontOfPawn2 = Pawn([2,2],'black')
        newBoard = ChessBoard()
        newBoard._addPiece(pawnCenterOfBoard)
        newBoard._addPiece(pawnBlackInfrontOfPawn)
        newBoard._addPiece(pawnBlackInfrontOfPawn2)
        #black movement
        tarPiece = newBoard.getPieceAtPosition([6,4])
        self.assertIsInstance(tarPiece,Pawn)
        possibleMoves = tarPiece.getPossibleMoves(newBoard)
        self.assertEqual(possibleMoves, [[5,4]])
        #diagnal movement and white movement
        tarPiece = newBoard.getPieceAtPosition([1,3])
        self.assertIsInstance(tarPiece,Pawn)
        possibleMoves = tarPiece.getPossibleMoves(newBoard)
        self.assertEqual(len(possibleMoves),3)
        expectedMoves =[[2,4],[2,3],[2,2]]
        for i in range(len(possibleMoves)):
            self.assertIn(expectedMoves[i],possibleMoves)
        #off the board movement
        tarPiece = newBoard.getPieceAtPosition([7,7])
        newBoard._removePiece(tarPiece)
        tarPiece = newBoard.getPieceAtPosition([1,3])
        newBoard._addPiece(tarPiece,[7,7])
        possibleMoves = tarPiece.getPossibleMoves(newBoard)
        self.assertEqual(possibleMoves, [])
        #blocked by piece
        newBoard._addPiece(pawnBlackInfrontOfPawn,[5,0])
        tarPiece = newBoard.getPieceAtPosition([6,0])
        possibleMoves = tarPiece.getPossibleMoves(newBoard)
        self.assertEqual(possibleMoves, [])
        newBoard.destructor()

class TestKnight(unittest.TestCase):
    print("running knight tests")
    def test_possibleMoves(self):
        newBoard=ChessBoard()
        newBoard.clearBoard()
        testKnight = Knight([4,4],'white')
        newBoard._addPiece(testKnight)
        #all 8 knight moves
        expectedMoves=[[6,3],[6,5],[5,2],[5,6],[3,2],[3,6],[2,3],[2,5]]
        actualMoves = testKnight.getPossibleMoves(newBoard)
        self.assertEqual(len(actualMoves),len(expectedMoves))
        for i in range(len(expectedMoves)):
            self.assertIn(expectedMoves[i],actualMoves)
        #moves off the board and allied pieces blocking
        newBoard.destructor()
        newBoard = newBoard=ChessBoard()
        testKnight = Knight([5,7],'white')
        testPawn = Pawn([3,6],'white')
        newBoard._addPiece(testKnight)
        newBoard._addPiece(testPawn)
        actualMoves = testKnight.getPossibleMoves(newBoard)
        expectedMoves=[[7,6],[6,5],[4,5]]
        self.assertEqual(len(actualMoves),len(expectedMoves))
        for i in range(len(expectedMoves)):
            self.assertIn(expectedMoves[i],actualMoves)
        newBoard.destructor()

class TestBishop(unittest.TestCase):
    print("running bishop tests")
    def test_possibleMoves(self):
        newBoard=ChessBoard()
        #at position 4,6 Bishop can potentially move off the board to the right, and goes through multiple enemies and allies on the left
        testBishop = Bishop([4,6],'white')
        newBoard._addPiece(testBishop)
        actualMoves = testBishop.getPossibleMoves(newBoard)
        expectedMoves = [[6,4],[5,5],[5,7],[3,5],[3,7],[2,4]]
        self.assertEqual(len(actualMoves), len(expectedMoves))
        for i in range(len(expectedMoves)):
            self.assertIn(expectedMoves[i],actualMoves)

class TestQueen(unittest.TestCase):
    print("running queen tests")
    def test_possibleMoves(self): 
        newBoard=ChessBoard()
        blockingTestPawn = Pawn([4,2],'white')
        testQueen = Queen([4,6],'white')
        newBoard._addPiece(testQueen)
        newBoard._addPiece(blockingTestPawn)
        actualMoves = testQueen.getPossibleMoves(newBoard)
        expectedMoves = [[6,4],[5,5],[5,7],[3,5],[3,7],[2,4],[4,3],[4,4],[4,5],[4,7],[6,6],[5,6],[3,6],[2,6]]
        self.assertEqual(len(actualMoves), len(expectedMoves))
        for i in range(len(expectedMoves)):
            self.assertIn(expectedMoves[i],actualMoves)

class TestRook(unittest.TestCase):
    print("running rook tests")
    def test_possibleMoves(self):
        newBoard=ChessBoard()
        blockingTestPawn = Pawn([4,2],'white')
        testRook = Rook([4,6],'white')
        newBoard._addPiece(testRook)
        newBoard._addPiece(blockingTestPawn)
        actualMoves = testRook.getPossibleMoves(newBoard)
        expectedMoves = [[4,3],[4,4],[4,5],[4,7],[6,6],[5,6],[3,6],[2,6]]
        self.assertEqual(len(actualMoves), len(expectedMoves))
        for i in range(len(expectedMoves)):
            self.assertIn(expectedMoves[i],actualMoves)


if __name__ == '__main__':
    unittest.main()
