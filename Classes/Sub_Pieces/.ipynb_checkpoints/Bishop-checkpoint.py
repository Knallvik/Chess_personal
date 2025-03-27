from Classes import Piece
from Classes import Board

class Bishop(Piece):
    def __init__(self, position_x, position_y, color):
        Piece.__init__(self, position_x, position_y, color)

    def scan_board(self, board):
        coordinates = dict()
        #scan north-east:
        i = 1
        not_end = True
        while not_end and self.position_y+i<Board.get_lim() and self.position_x+i<Board.get_lim():
            try:
                color = board[self.position_x+i][self.position_y+i].color
            except:
                coordinates[self.position_x+i,self.position_y+i] = True
            else:
                if color!= self.color:
                    coordinates[self.position_x+i,self.position_y+i] = True
                not_end = False
            i+=1

        #scan south-east:
        i = 1
        not_end = True
        while not_end and self.position_x+i<Board.get_lim() and self.position_y-i>=0:
            try:
                color = board[self.position_x+i][self.position_y-i].color
            except:
                coordinates[self.position_x+i,self.position_y-i] = True
            else:
                if color!= self.color:
                    coordinates[self.position_x+i,self.position_y-i] = True
                not_end = False
            i+=1
        #scan south-west:
        i = 1
        not_end = True
        while not_end and self.position_y-i>=0 and self.position_x-i>=0:
            try:
                color = board[self.position_x-i][self.position_y-i].color
            except:
                coordinates[self.position_x-i,self.position_y-i] = True
            else:
                if color!= self.color:
                    coordinates[self.position_x-i,self.position_y-i] = True
                not_end = False
            i+=1
        #scan north-west
        i = 1
        not_end = True
        while not_end and self.position_x-i>=0 and self.position_y+i<Board.get_lim():
            try:
                color = board[self.position_x-i][self.position_y+i].color
            except:
                coordinates[self.position_x-i,self.position_y+i] = True
            else:
                if color != self.color:
                    coordinates[self.position_x-i,self.position_y+i] = True
                not_end = False
            i+=1
        return coordinates
    
    def type(self):
        if self.color == 'white':
            return chr(0x2657) + ' ' #white bishop
        else:
            return chr(0x265D) + ' ' #black bishop

    def __str__(self):
        return self.type()