from Figure_module import Figure

class Rhombus(Figure):
    def __init__(self,a,b,h):
        super().__init__(a,b,h)

    def Area(self):
        return self.a*self.h