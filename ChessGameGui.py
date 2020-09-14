import pygame
import os
import sys
import ChessPiecesandBoard
import time
import math


class ChessGUI:
    def __init__(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'
        pygame.init()
        pygame.display.init()
        self.screen = pygame.display.set_mode((850, 500))
        self.boardStart_x = 50
        self.boardStart_y = 50
        pygame.display.set_caption('Python Chess')
        self.fontDefault = pygame.font.Font(None, 20)
        self.LoadImages()

    def LoadImages(self):
        self.square_size = 50
        self.white_square = pygame.image.load(os.getcwd() +"\\images\\white_square.png").convert()
        self.brown_square = pygame.image.load(os.getcwd() +"\\images\\brown_square.png").convert()
        self.cyan_square = pygame.image.load(os.getcwd() +"\\images\\cyan_square.png").convert()
        self.black_pawn = pygame.image.load(os.getcwd() +"\\images\\Chess_tile_pd.png").convert()
        self.black_pawn = pygame.transform.scale(self.black_pawn, (self.square_size,self.square_size))
        self.black_rook = pygame.image.load(os.getcwd() +"\\images\\Chess_tile_rd.png").convert()
        self.black_rook = pygame.transform.scale(self.black_rook, (self.square_size,self.square_size))
        self.black_knight = pygame.image.load(os.getcwd() +"\\images\\Chess_tile_nd.png").convert()
        self.black_knight = pygame.transform.scale(self.black_knight, (self.square_size,self.square_size))
        self.black_bishop = pygame.image.load(os.getcwd() +"\\images\\Chess_tile_bd.png").convert()
        self.black_bishop = pygame.transform.scale(self.black_bishop, (self.square_size,self.square_size))
        self.black_king = pygame.image.load(os.getcwd() +"\\images\\Chess_tile_kd.png").convert()
        self.black_king = pygame.transform.scale(self.black_king, (self.square_size,self.square_size))
        self.black_queen = pygame.image.load(os.getcwd() +"\\images\\Chess_tile_qd.png").convert()
        self.black_queen = pygame.transform.scale(self.black_queen, (self.square_size,self.square_size))
        self.white_pawn = pygame.image.load(os.getcwd() +"\\images\\Chess_tile_pl.png").convert()
        self.white_pawn = pygame.transform.scale(self.white_pawn, (self.square_size,self.square_size))
        self.white_rook = pygame.image.load(os.getcwd() +"\\images\\Chess_tile_rl.png").convert()
        self.white_rook = pygame.transform.scale(self.white_rook, (self.square_size,self.square_size))
        self.white_knight = pygame.image.load(os.getcwd() +"\\images\\Chess_tile_nl.png").convert()
        self.white_knight = pygame.transform.scale(self.white_knight, (self.square_size,self.square_size))
        self.white_bishop = pygame.image.load(os.getcwd() +"\\images\\Chess_tile_bl.png").convert()
        self.white_bishop = pygame.transform.scale(self.white_bishop, (self.square_size,self.square_size))
        self.white_king = pygame.image.load(os.getcwd() +"\\images\\Chess_tile_kl.png").convert()
        self.white_king = pygame.transform.scale(self.white_king, (self.square_size,self.square_size))
        self.white_queen = pygame.image.load(os.getcwd() +"\\images\\Chess_tile_ql.png").convert()
        self.white_queen = pygame.transform.scale(self.white_queen, (self.square_size,self.square_size))

    def ConvertToScreenCoords(self, chessSquareTuple):
        # converts a (row,col) chessSquare into the pixel location of the upper-left corner of the square
        (row, col) = chessSquareTuple
        screenX = self.boardStart_x + col*self.square_size
        screenY = self.boardStart_y + row*self.square_size
        return (screenX, screenY)

    def ConvertToChessCoords(self, screenPositionTuple):
        # converts a screen pixel location (X,Y) into a chessSquare tuple (row,col)
        # x is horizontal, y is vertical
        # (x=0,y=0) is upper-left corner of the screen
        (X, Y) = screenPositionTuple
        row = math.floor(((Y-self.boardStart_y) / self.square_size))
        col = math.floor(((X-self.boardStart_x) / self.square_size))
        return (row, col)

    def Draw(self, board, highlightSquares=[]):
        self.screen.fill((0, 0, 0))
        boardSize = len(board)

        # draw blank board
        for r in range(boardSize):
            startWhite = r % 2
            if startWhite:
                current_square = 1
            else: 
                current_square = 0

            for c in range(boardSize):
                (screenX, screenY) = self.ConvertToScreenCoords((r, c))
                if current_square:
                    self.screen.blit(self.brown_square, (screenX, screenY))
                    current_square = (current_square+1) % 2
                else:
                    self.screen.blit(self.white_square, (screenX, screenY))
                    current_square = (current_square+1) % 2


        #chessboard_obj = ChessBoard()
        color = (0,0,0)#white
        antialias = 1
        
        # top and bottom - display cols
        #for c in range(boardSize):
        #    for r in [-1,boardSize]:
        #        (screenX,screenY) = self.ConvertToScreenCoords((r,c))
        #        screenX = screenX + self.square_size/2
        #        screenY = screenY + self.square_size/2
        #        #notation = chessboard_obj.ConvertToAlgebraicNotation_col(c)
        #        renderedLine = self.fontDefault.render("a",antialias,color)
        #        self.screen.blit(renderedLine,(screenX,screenY))
        
        # left and right - display rows
        #for r in range(boardSize):
        #    for c in [-1,boardSize]:
        #        (screenX,screenY) = self.ConvertToScreenCoords((r,c))
        #        screenX = screenX + self.square_size/2
        #        screenY = screenY + self.square_size/2
        #        # notation = chessboard_obj.ConvertToAlgebraicNotation_row(r)
        #        renderedLine = self.fontDefault.render("b",antialias,color)
        #        self.screen.blit(renderedLine,(screenX,screenY))
                
        # highlight squares if specified
        for square in highlightSquares:
            (screenX,screenY) = self.ConvertToScreenCoords(square)
            self.screen.blit(self.cyan_square,(screenX,screenY))
        
        # draw pieces
        for r in range(boardSize):
            for c in range(boardSize):
                (screenX,screenY) = self.ConvertToScreenCoords((r,c))
                if board[r][c] == 'bP':
                    self.screen.blit(self.black_pawn,(screenX,screenY))
                if board[r][c] == 'bR':
                    self.screen.blit(self.black_rook,(screenX,screenY))
                if board[r][c] == 'bT':
                    self.screen.blit(self.black_knight,(screenX,screenY))
                if board[r][c] == 'bB':
                    self.screen.blit(self.black_bishop,(screenX,screenY))
                if board[r][c] == 'bQ':
                    self.screen.blit(self.black_queen,(screenX,screenY))
                if board[r][c] == 'bK':
                    self.screen.blit(self.black_king,(screenX,screenY))
                if board[r][c] == 'wP':
                    self.screen.blit(self.white_pawn,(screenX,screenY))
                if board[r][c] == 'wR':
                    self.screen.blit(self.white_rook,(screenX,screenY))
                if board[r][c] == 'wT':
                    self.screen.blit(self.white_knight,(screenX,screenY))
                if board[r][c] == 'wB':
                    self.screen.blit(self.white_bishop,(screenX,screenY))
                if board[r][c] == 'wQ':
                    self.screen.blit(self.white_queen,(screenX,screenY))
                if board[r][c] == 'wK':
                    self.screen.blit(self.white_king,(screenX,screenY))
            
        pygame.display.flip()

if __name__ == "__main__":
    testBoard = [['bR','bT','bB','bQ','bK','bB','bT','bR'],\
                ['bP','bP','bP','bP','bP','bP','bP','bP'],\
                ['e','e','e','e','e','e','e','e'],\
                ['e','e','e','e','e','e','e','e'],\
                ['e','e','e','e','e','e','e','e'],\
                ['e','e','e','e','e','e','e','e'],\
                ['wP','wP','wP','wP','wP','wP','wP','wP'],\
                ['wR','wT','wB','wQ','wK','wB','wT','wR']]
                    
    validSquares = [(1,2),(1,1),(0,0),(7,7)]

    game = ChessGUI()
    game.Draw(testBoard,validSquares)
    time.sleep(30)