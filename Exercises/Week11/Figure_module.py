class Figure:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def Area(self):
        return "Area of Figure!"

    def __str__(self):
        return ("I'm {} and I have {} m**2 area!".format(type(self).__name__, self.Area()))