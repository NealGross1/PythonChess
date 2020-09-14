from ChessGameGui import *
from ChessPiecesandBoard import *
import pygame
import sys

#start game and GUI
Game = ChessBoard()
GUI = ChessGUI() 
boardDescription = getBoardDescription(Game)     
validSquares = []
GUI.Draw(boardDescription,validSquares)
GameIsOver = False
currentPlayer = 'white'
currentCoordinates = (-1,-1)
targetPiece = None
movePiece = None
moves = []
listMoves = []
Debug = False

while not GameIsOver:

#player selection
#Alternate Turns
#announce check or check mate --> end Game
    for event in pygame.event.get():
        ##CLICK EVENT##
        if event.type == 5:
            if Debug:
                print("click event")
            mouseCoordinates = pygame.mouse.get_pos()
            RowCol = GUI.ConvertToChessCoords(mouseCoordinates)
            #ignore clicks outside the board
            ##SELECT SAME PIECE AGAIN##
            if currentCoordinates == RowCol:
                if Debug:
                    print("same piece")
                #do nothing
                pass

            ##SELECT PIECE ON BOARD##
            elif not (RowCol[0] < 0 or RowCol[0] >7 or RowCol[1]<0 or RowCol[1] >7):
                if Debug:
                    print ("clicked on board")
                ##SELECT A DIFFERENT PIECE##
                if currentCoordinates != RowCol:
                    ##IN POSSIBLE MOVES##
                    if Debug:
                        print ("clicked different piece")
                    if RowCol in moves and not (type(targetPiece) == int or targetPiece == None):
                        if Debug:
                            print ("valid move")
                        movePiece = Game.getPieceAtPosition(RowCol)
                        ##ENEMY OR EMPTY SPACE## 
                        if type(movePiece) == int: 
                            pass
                        elif not (movePiece.color == currentPlayer) :
                            pass
                        else:
                            #targeting own piece?
                            continue 

                        #call game function to make move 
                        Game.movePiece(currentCoordinates, RowCol)
                        #update board GUI based on board
                        GUI.Draw(getBoardDescription(Game),[])
                        listMoves =[]
                        moves=[]
                        #next players turn 
                        if currentPlayer == 'white':
                            currentPlayer = 'black'
                        else: 
                            currentPlayer = 'white'
                        continue
                    ##NOT A POSSIBLE MOVE##
                    else:
                        if Debug:
                            print ("not a valid move")
                        currentCoordinates = RowCol
                        targetPiece = Game.getPieceAtPosition(RowCol)
                        ##NOT ENEMY PIECE##
                        if not type(targetPiece) == int or targetPiece == None:
                            if Debug:
                                print ("selected chess piece")
                            if targetPiece.color == currentPlayer: 
                                if Debug:
                                   print ("chess curr player")
                                listMoves=[]
                                listMoves = targetPiece.getPossibleMoves(Game)
                                moves = []
                                for l in listMoves:
                                    moves.append(tuple(l))                         
                        ##CLEAR PREVIOUS SELECTION
                        else:
                            if Debug:
                                print ("clearing selection")
                            currentCoordinates = (-1,-1)
                            targetPiece = None
                            movePiece = None
                            moves = []
                            listMoves = []
                        ##UPDATE UI##
                        boardDescription = getBoardDescription(Game) 
                        GUI.Draw(getBoardDescription(Game),moves)
                #CLICKING ON SAME PIECE
                else:
                    boardDescription = getBoardDescription(Game)     
                    validSquares = []
                    GUI.Draw(boardDescription,validSquares)
            ##CLICK NOT ON BOARD##
            else:
                boardDescription = getBoardDescription(Game)     
                validSquares = []
                GUI.Draw(boardDescription,validSquares)
        ##ESCAPE KEY KEYBOARD EVENT##
        if event.type == 3:
            GameIsOver = True


     #announce winner play again 