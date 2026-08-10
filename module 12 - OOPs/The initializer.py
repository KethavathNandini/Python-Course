# __init__ method
# is an instance method
# is used to create and initialize the attribute during the object creation

class Student:

    def __init__(self, name, id):
        print(f"calling initializer for {self}")
        self.name = name
        self.id = id


    def study(self):
        print(self)
        print("Hello there!")


s1 = Student("carel" ,188)

s2 = Student("john" , 1003)

print(s1.__dict__)
print(s2.__dict__)