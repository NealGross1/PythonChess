from ChessGameGui import *
from ChessPiecesandBoard import *
import pygame
import sys

#start game and GUI
Game = ChessBoard()
GUI = ChessGUI() 

GameIsOver = False
currentPlayerColor = 'white'
currentCoordinates = (-1,-1)
targetPiece = None
movePiece = None
moves = []
listMoves = []
Debug = False


class ChessGameInterface:
    def __init__(self, startingColor, chessBoard, GUI):
        self.currentPlayer = startingColor
        self.selectedPiece = None
        self.selectedPieceCoordinates = [-1,-1]
        self.clickedPiece = None
        self.gameIsOver = False
        self.selectedPieceMoves = []
        self.GUI = GUI
        self.Game = chessBoard
        self.currentPlayerInCheck = False
        self.checkMoves = []

    def updateUI(self):
        boardDescription = getBoardDescription(self.Game)

        if self.selectedPiece == None or type(self.selectedPiece) == int:
            self.GUI.Draw(boardDescription,[])
            return

        self.selectedPieceMoves = []
        listMoves = self.selectedPiece.getPossibleMoves(self.Game)
        for move in listMoves:
            self.selectedPieceMoves.append(tuple(move))  

        self.GUI.Draw(boardDescription,self.selectedPieceMoves)

    def nextTurn(self):
        self.selectedPiece = None
        self.selectedPieceMoves = []
        self.selectedPieceCoordinates = []
        self.checkMoves = []
        #next players turn 
        if self.currentPlayer == 'white':
            self.currentPlayer = 'black'
        else:
            self.currentPlayer = 'white'
        self.currentPlayerInCheck = self.Game.isCheck(self.currentPlayer)
        if self.currentPlayerInCheck:
            for move in self.Game.movesToGetOutofCheck(self.currentPlayer): 
                self.checkMoves.append(tuple(move)) 
        else: 
            self.checkMoves = []
        
        if self.currentPlayerInCheck and len(self.checkMoves) == 0:
            self.gameIsOver = True
        self.updateUI()



GameInterface = ChessGameInterface('white', Game, GUI)
GameInterface.updateUI()

while not GameInterface.gameIsOver:
    for event in pygame.event.get():
        ##CLICK EVENT##
        if event.type == 5:
            mouseCoordinates = pygame.mouse.get_pos()
            RowCol = GameInterface.GUI.ConvertToChessCoords(mouseCoordinates)
            ##SELECT SAME PIECE AGAIN##
            if GameInterface.selectedPieceCoordinates == RowCol:
                #do nothing
                continue

            ##SELECT PIECE ON BOARD##
            elif not (RowCol[0] < 0 or RowCol[0] >7 or RowCol[1]<0 or RowCol[1] >7):
                GameInterface.clickedPiece = GameInterface.Game.getPieceAtPosition(RowCol)
                ##HAVE A PREVIOUSLY SELECTED PIECE##
                if not type(GameInterface.selectedPiece) == int or GameInterface.selectedPiece == None:
                    ##MOVE TO GET OUT OF CHECK
                    if GameInterface.currentPlayerInCheck: 
                        ##MAKE MOVE TO GET OUT OF CHECK
                        if RowCol in GameInterface.checkMoves:
                            putsIntoCheck = GameInterface.Game.movePutsPlayerIntoCheck(GameInterface.currentPlayer,GameInterface.selectedPieceCoordinates, RowCol)
                            if putsIntoCheck:
                                print ('invalid move to:', RowCol)
                                print ('possible moves are:',  GameInterface.checkMoves)
                                ##TODO NOTIFY USER##
                                continue
                            else:
                                GameInterface.Game.movePiece(GameInterface.selectedPieceCoordinates, RowCol)
                                GameInterface.nextTurn()
                        elif type(GameInterface.clickedPiece) != int and GameInterface.clickedPiece != None:
                            if GameInterface.clickedPiece.color == GameInterface.currentPlayer:
                                GameInterface.selectedPiece = GameInterface.clickedPiece
                                GameInterface.selectedPieceCoordinates = RowCol
                                GameInterface.updateUI()
                        ##INVALID MOVE##
                        else:
                            print ('invalid move to:', RowCol)
                            print ('possible moves are:',  GameInterface.checkMoves)
                            ##TODO NOTIFY USER##
                            continue

                    ##NOT IN CHECK MAKE MOVE IF YOUR PIECE##
                    elif RowCol in GameInterface.selectedPieceMoves:
                        ##CANT MOVE YOURSELF INTO CHECK##
                        putsIntoCheck = GameInterface.Game.movePutsPlayerIntoCheck(GameInterface.currentPlayer,GameInterface.selectedPieceCoordinates, RowCol)
                        if putsIntoCheck:
                            #tell user
                            print ("you can't move yourself into check")
                            continue
                        GameInterface.Game.movePiece(GameInterface.selectedPieceCoordinates, RowCol)
                        GameInterface.nextTurn()
                    ##NOT IN CHECK SELECT EMPTY OR OWN PIECE##
                    elif type(GameInterface.clickedPiece) != int or GameInterface.clickedPiece == None:
                        if GameInterface.clickedPiece.color == GameInterface.currentPlayer:
                            GameInterface.selectedPiece = GameInterface.clickedPiece
                            GameInterface.selectedPieceCoordinates = RowCol
                            GameInterface.updateUI()

                ##DON'T HAVE A SELECTED PIECE##
                elif type(GameInterface.clickedPiece) != int or GameInterface.clickedPiece == None:
                    if GameInterface.clickedPiece.color == GameInterface.currentPlayer:
                        #make the piece selected 
                        GameInterface.selectedPiece = GameInterface.clickedPiece
                        GameInterface.selectedPieceCoordinates = RowCol
                        GameInterface.updateUI()

        if event.type == 3:
            print ('game is ending')
            GameInterface.gameIsOver = True

print ('has won the game!')
