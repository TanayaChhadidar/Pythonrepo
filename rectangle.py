class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calculate_area(self):
        print("Area:", self.length * self.breadth)


r1 = Rectangle(10, 5)
r1.calculate_area()