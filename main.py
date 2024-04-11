from Classes import *

def assemble_board():
    board = Board()
    board.add_piece(King(position_x=4, position_y=0, color='white'))
    board.add_piece(King(position_x=4, position_y=7, color='black'))
    board.add_piece(Queen(position_x=3, position_y=0, color='white'))
    board.add_piece(Queen(position_x=3, position_y=7, color='black'))
    for i in range(8):
        board.add_piece(Pawn(position_x=i, position_y=1, color='white'))
        board.add_piece(Pawn(position_x=i, position_y=6, color='black'))
    for i in range(2):
        board.add_piece(Tower(position_x=i*7, position_y=0, color='white'))
        board.add_piece(Tower(position_x=i*7, position_y=7, color='black'))
        board.add_piece(Knight(position_x=1+i*5, position_y=0, color='white'))
        board.add_piece(Knight(position_x=1+i*5, position_y=7, color='black'))
        board.add_piece(Bishop(position_x=2+i*3, position_y=0, color='white'))
        board.add_piece(Bishop(position_x=2+i*3, position_y=7, color='black'))
    return board

def play_game():
    board = assemble_board()
    i = 0
    while board.continue_game:
        print(board)
        i+= 1 # to compare with boards counter, only continue if the counters match,
        #indicating that a move has been made
        while i>board.number_moves:
            if i%2 == 1:
                # terminal inputs are a string
                x_start, y_start = input('choose a piece to move, White: ') #e.g d2
                x_end, y_end = input('choose where to move it, White: ') #e.g d4
            else:
                x_start, y_start = input('choose a piece to move, Black: ') #e.g d2
                x_end, y_end = input('choose where to move it, Black: ') #e.g d4
            board.move_piece([x_start, int(y_start)-1],[x_end, int(y_end)-1])
    print(board)
            

if __name__ == '__main__':

    play_game()
