class Board():
    def __init__(self):
        #Give attributes to be used in the game
        self.continue_game = True
        #self.winner = None
        self.number_moves = 0
        self.check_white = False
        self.check_black = False
        #Choose which player is to move
        self.to_move = 'white'
        #List the names of the columns
        self.x_plane = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        #Get the pieces objects we are playing with
        self.inhabitant = [[None for i in range(Board.get_lim())] for i\
                            in range(Board.get_lim())]
        #Get the names of the pieces that are used in the __str__ representation
        self.tiles = [["  " for i in range(Board.get_lim())] \
                      for i in range(Board.get_lim())]
    
    #Set the max limit (-1) in the x-y direction
    @staticmethod
    def get_lim():
        return 8
    
    #Translate the column name to a usable index
    def translate_str_to_index(self, str):
        if not str in self.x_plane:
            return 'invalid letter'
        for i, letter in enumerate(self.x_plane):
            if str == letter:
                id = i
        return id

    #Add a piece to the board
    def add_piece(self, piece):
        #Add the object we are using
        self.inhabitant[piece.position_x][piece.position_y] = piece
        #Add the appropriate str to be printed
        self.tiles[piece.position_x][piece.position_y] = piece.type()

    #Check for legal moves
    def legal_moves(self, piece, bypass = False):
        scans = piece.scan_board(self)
        legal_move = []
        # Check doesnt require an actual legal move, hence the bypass;
        # bypassing the else-statment that checks if you can move the piece
        # without exposing the king.
        if bypass:
            for key in scans:
                legal_move.append(key)
        else:
            for key in scans:
                # store present values
                x, y = piece.position_x, piece.position_y
                piece.position_x = key[0]
                piece.position_y = key[1]
                piece2 = self.inhabitant[key[0]][key[1]]
                statement_white = self.check_white
                statement_black = self.check_black
                
                #Make one of the valid moves
                self.inhabitant[key[0]][key[1]] = piece
                self.inhabitant[x][y] = None
                #See if the moves exposes your king
                self.is_check()
                #Add the move to legal moves if it doesnt expose it
                if piece.color == 'white' and not self.check_white:
                    legal_move.append(key)
                elif piece.color == 'black' and not self.check_black:
                    legal_move.append(key)
                #return board as it was
                piece.position_x, piece.position_y = x, y
                self.inhabitant[x][y] = piece
                self.inhabitant[key[0]][key[1]] = piece2
                self.check_black = statement_black
                self.check_white = statement_white


        return legal_move
    
    #Check if one of the kings are in the legal moves of one of the opponents pieces
    def is_check(self):
        #Loop over all objects in the board
        for pieces in self.inhabitant:
            for piece in pieces:
                #Get the legal moves of the piece-objects on the board 
                #(the rest are None-type objects)
                try:
                    legal_moves = self.legal_moves(piece, bypass = True)
                except:
                    pass
                #If the piece has a method giving it its legal moves
                #(Try-statement doesnt throw a fit (error))
                else:
                    for move in legal_moves:
                        #Check if the king exists in the legal moves of the piece
                        try:
                            is_king = self.inhabitant[move[0]][move[1]].is_king
                        except:
                            pass
                        #If the piece is a King;
                        #If the color of the king is white and the piece that has it in
                        #its legal moves is black, say white is in check and return
                        else:
                            if is_king and self.inhabitant[move[0]][move[1]]\
                                .color == 'white' and piece.color == 'black':
                                self.check_white = True
                                return
                            #If it isnt in check, return False and keep going.
                            #If no black pieces has the white king in check, it returns False.
                            else:
                                self.check_white = False
                            #If the color of the king is black and the piece that has it in
                            #its legal moves is white, say black is in check and return
                            if is_king and self.inhabitant[move[0]][move[1]]\
                                .color == 'black' and piece.color == 'white':
                                self.check_black = True
                                return
                            else:
                                self.check_black = False
        return

    #Check if there is check_mate, if there is check
    def check_mate(self, color_check):
        #color_check is black or white, str
        #Loop over all pieces on the board
        for pieces in self.inhabitant:
            for piece in pieces:
                #See if the object has a color (as all pieces do, the other objects are None-type)
                try:
                    color = piece.color
                except:
                    pass
                #For that piece
                else:
                    #If the color of the pieces is the same as the king in check;
                    if color == color_check:
                        #Get all legal moves for the piece
                        legal_moves = self.legal_moves(piece)
                        #store position for the piece for later
                        x, y = piece.position_x, piece.position_y
                        #Loop over all legal moves for the piece to see if it can stop the check
                        for moves in legal_moves:
                            #Take the piece to a legal move
                            piece.position_x = moves[0]
                            piece.position_y = moves[1]
                            piece2 = self.inhabitant[moves[0]][moves[1]]
                            self.inhabitant[moves[0]][moves[1]] = piece
                            self.inhabitant[x][y] = None
                            #Store the current check values
                            check_white = self.check_white
                            check_black = self.check_black
                            #Check if black or white is in check after moving
                            self.is_check()
                            #If white was in check and the movement of the piece (white) 
                            #can stop it, return False (not check mate)
                            if not self.check_white and color_check=='white':
                                #Return the values to normal (we dont wanna make
                                #changes to the board)
                                self.check_white = check_white
                                self.check_black = check_black
                                piece.position_x = x
                                piece.position_y = y
                                self.inhabitant[moves[0]][moves[1]] = piece2
                                self.inhabitant[x][y] = piece
                                return False
                            #Else if black was in check and the piece (black) can stop it,
                            #return False
                            elif not self.check_black and color_check=='black':
                                #Return the values to normal (we dont wanna make
                                #changes to the board)
                                self.check_white = check_white
                                self.check_black = check_black
                                piece.position_x = x
                                piece.position_y = y
                                self.inhabitant[moves[0]][moves[1]] = piece2
                                self.inhabitant[x][y] = piece
                                return False
                            #Return the values to normal (we dont wanna make
                            #changes to the board, in case the other king was put in check)
                            self.check_white = check_white
                            self.check_black = check_black
                            piece.position_x = x
                            piece.position_y = y
                            self.inhabitant[moves[0]][moves[1]] = piece2
                            self.inhabitant[x][y] = piece
        return True

    def move_piece(self, start: list, end: list):
        # x-axis is letters on a checkboard, but allow numbers as well
        if type(start[0]) == str:
            id_x_start = self.translate_str_to_index(start[0].upper())
            if id_x_start == 'invalid letter':
                print(id_x_start)
                return
        else:
            id_x_start = start[0]

        if type(end[0]) == str:
            id_x_end = self.translate_str_to_index(end[0].upper())
            if id_x_end == 'invalid letter':
                print(id_x_end)
                return
        else:
            id_x_end = end[0]
        
        #See that an actual piece is chosen to move
        if bool(self.inhabitant[id_x_start][start[1]]):
            piece = self.inhabitant[id_x_start][start[1]]
        else:
            print("No piece here")
            return
        
        #See that the correct player is moving the piece
        if self.to_move == 'white' and self.inhabitant[id_x_start][start[1]].color != 'white':
            print('Not your turn')
            return
        elif self.to_move == 'black' and self.inhabitant[id_x_start][start[1]].color != 'black':
            print('Not your turn')
            return
        #Check the legal moves of the piece chosen
        legal_moves = self.legal_moves(piece)
        print(legal_moves)
        if (id_x_end,end[1]) in legal_moves:
            print("You Chose a Legal Move")

            #Move the piece object
            self.inhabitant[id_x_end][end[1]] = piece
            self.inhabitant[id_x_start][start[1]] = None

            #Update the representable
            self.tiles[id_x_end][end[1]] = piece.type()
            self.tiles[id_x_start][start[1]] = "  "
            #Update position of the moved piece
            piece.position_x = id_x_end
            piece.position_y = end[1]
            #Update move-counter, to be compared in play-function in main.py
            self.number_moves += 1
            #Some pieces care if they have been moved previously
            try:
                moved = piece.been_moved
            except:
                pass
            else:
                if not moved:
                    piece.been_moved = True
            #See if the move resulted in check
            self.is_check()
            #for debugging
            print('white check: ', self.check_white, 'black check: ', self.check_black)
            if self.check_white:
                print('White has been checked')
                #See if the check is a check mate
                if self.check_mate('white'):
                    self.continue_game = False
                    print(f'Black Wins in {self.number_moves} moves')

            elif self.check_black:
                print('Black has been checked')
                if self.check_mate('black'):
                    self.continue_game = False
                    print(f'White Wins in {self.number_moves} moves')

            #Change who is to move
            if self.to_move == 'white':
                self.to_move = 'black'
            else:
                self.to_move = 'white'
        #If move is not legal
        else:
            print("Not allowed! Learn the rules.")
    #Get items of the board
    def __getitem__(self, indices):
        try:
            item = self.inhabitant[indices[0]][indices[1]]
        except:
            item = self.inhabitant[indices]
        finally:
            return item

    #Print the checkboard
    def __str__(self):
        str = " "
        #x-plane, first line
        for i in range(Board.get_lim()):
            str+= f" {self.x_plane[i]} "
        str += "\n"
        #y-plane
        for i in range(Board.get_lim()):
            str += f"{i+1}|"
            #x-plane
            for j in range(Board.get_lim()):
                str += self.tiles[j][i] + "|"
            if i<7:
                str += "\n -"
                for j in range(Board.get_lim()):
                    str+= "---"
            str+="\n"

        return str