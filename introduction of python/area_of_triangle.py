'''
area of trinagle when all lenght of the sides are known - a, b , c
semi perimeter (s) = (a + b + c) / 2
area = square root of (s * (s - a) * (s - b) * (s - c))
'''
a = float(input("Enter the length of first side : "))
b = float(input("Enter the length of second side : "))
c = float(input("Enter the length of third side : "))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("Area of triangle : ",area)