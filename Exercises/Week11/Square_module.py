from Figure_module import Figure

class Square(Figure):

    def __init__(self, a, b, h):
        super().__init__(a, b, h)

    def Area(self):
        return self.a*self.b