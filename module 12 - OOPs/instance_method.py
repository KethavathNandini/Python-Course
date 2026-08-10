# Instances method
#  method defined inside a class which is bound to/ associated with the instance/object


class Student:
    def study(self):
        print(self)
        print("Hello there!")


s1 = Student()
print(s1)
s1.study()

"""When we call an instance method using the object/instance of the class, python passes the object itself as the 
first argument to that method
The first argument is by standard is self
"""
