from Classes import Piece

class Pawn(Piece):
    def __init__(self, position_x, position_y, color):
        self.been_moved = False
        Piece.__init__(self, position_x, position_y, color)
        
    def scan_board(self, board):
        coordinates = dict()
        if self.color == 'white':
            try:
                color = board[self.position_x+1][self.position_y+1].color
            except:
                pass
            else:
                if color != self.color:
                    coordinates[self.position_x+1,self.position_y+1] = True
                    
            try:
                color = board[self.position_x-1][self.position_y+1].color
            except:
                pass
            else:
                if color != self.color:
                    coordinates[self.position_x-1,self.position_y+1] = True

            if not bool(board[self.position_x][self.position_y+1]):
                coordinates[(self.position_x,self.position_y+1)] = True

            if not self.been_moved and (self.position_x,self.position_y+1) in coordinates:
                if not bool(board[self.position_x][self.position_y+2]):
                    coordinates[(self.position_x,self.position_y+2)] = True

        else:
            try:
                color = board[self.position_x+1][self.position_y-1].color
            except:
                pass
            else:
                if color != self.color:
                    coordinates[self.position_x+1,self.position_y-1] = True
            try:
                color = board[self.position_x-1][self.position_y-1].color
            except:
                pass
            else:
                if color != self.color:
                    coordinates[self.position_x-1,self.position_y-1] = True

            if not bool(board[self.position_x][self.position_y-1]):
                coordinates[(self.position_x,self.position_y-1)] = True

            if not self.been_moved and (self.position_x,self.position_y-1) in coordinates:
                if not bool(board[self.position_x][self.position_y-2]):
                    coordinates[(self.position_x,self.position_y-2)] = True

        return coordinates
        
    def transform(self):
        # Turn pawn into other chess object
        pass

    def type(self):
        if self.color == 'white':
            return chr(0x265F) + ' ' #black Pawn
        else:
            return chr(0x2659) + ' ' #pawn

    def __str__(self):
        return self.type()