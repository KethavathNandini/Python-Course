# creating a class
# dunder -double underscore
# creating an object
# calling method using objects?
# obj.method(args1, arg2,arg3.....)

class Student:
    """
    let's start the day with a positive hope
    """
    pass

s1 = Student()
s2 = Student()


s1.name = "Mikasa"
s1.id = 81018

print(s1.name)
print(s1.id)
print(s1.__dict__)
print(s2.__dict__)



# Doc string => __doc__(dunder)
'''
print(Student.__doc__)
print(help(Student))
'''
