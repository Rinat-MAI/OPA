class Square:

    all_rectangles = []

    def __init__(self, height, width=0):
        if width == 0:
            self.height = height
            self.width = height
        Square.all_rectangles.append(self)


    def Set_height(self, height):
        self.height = height

    def Get_height(self, height):
        return self.height

    @classmethod
    def all_area(cls):
        total_area = 0
        for figure in cls.all_rectangles:
            total_area += figure.area(figure.height, figure.width)
        return total_area

    @staticmethod
    def area(width, height):
        return width * height


class Rectangle(Square):
    def __init__(self, height, width):
        self.width = width
        self.height = height
        Square.all_rectangles.append(self)


a = Rectangle(12, 13)
b = Square(4)
print("Area:", a.area(a.width, a.height))
print(Square.all_area())