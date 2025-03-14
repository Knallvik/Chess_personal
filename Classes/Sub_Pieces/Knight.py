from Classes import Piece
from Classes import Board

class Knight(Piece):
    def __init__(self, position_x, position_y, color):
        Piece.__init__(self, position_x, position_y, color)

    def scan_board(self, board):
        coordinates = dict()
        moves = [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]
        for move in moves:
            if self.position_x+move[0]>=0 and self.position_x+move[0]<Board.get_lim()\
            and self.position_y+move[1]>=0 and self.position_y+move[1]<Board.get_lim():
                try:
                    color = board[self.position_x+move[0]][self.position_y+move[1]].color
                except:
                    coordinates[self.position_x+move[0],self.position_y+move[1]] = True
                else:
                    if color != self.color:
                        coordinates[self.position_x+move[0],self.position_y+move[1]] = True
        return coordinates
    
    def type(self):
        if self.color == 'white':
            return chr(0x265E) + ' ' #black horse, so not as to confuse with king
        else:
            return chr(0x2658) + ' ' #white horse, so not as to confuse with king

    def __str__(self):
        return self.type()