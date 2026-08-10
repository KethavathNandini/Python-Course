class Rectangle:
    def __init__(self, length , breadth):
        self.length = length
        self.breadth = breadth


    def area(self):
        return self.length * self.breadth


    def __add__(self, other):
        return self.length + other.length , self.breadth + other.breadth


r1 = Rectangle(4,4)
r2 = Rectangle(3,4)

print(r1.area())
print(r2.area())

print(r1 + r2 )