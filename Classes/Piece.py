class Piece():
    def __init__(self, position_x: int, position_y: int, color: str):
        self.color = color.lower()
        self.is_king = False
        if self.color != 'white' and self.color!='black':
            raise ValueError("Must choose Black or White color")
        self.position_x = position_x
        self.position_y = position_y

    def get_position_x(self):
        return self.position_x
    
    def get_position_y(self):
        return self.position_y
    
    def get_color(self):
        return self.color