from Classes import Piece
from Classes import Board

class King(Piece):
    def __init__(self, position_x, position_y, color):
        self.been_moved = False
        Piece.__init__(self, position_x, position_y, color)
        self.is_king = True

    def scan_board(self, board):
        coordinates = dict()
        moves = [(-1,-1), (-1,0), (-1,-1), (0,-1), (0,-1), (1,-1), (1,0), (1,1)]
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
            return chr(0x2654) + ' ' #white King
        else:
            return chr(0x265A) + ' ' #black King

    def __str__(self):
        return self.type()