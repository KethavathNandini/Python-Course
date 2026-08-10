"""
class variables are defined at the class level.
same copy of the class variable are shared among the objects
"""


class Student:

    college_name = "sree dattha institutions"
    department = ["CSE", "EEE", "CSBS", "AIML"]

    def __init__(self, name, roll):
        print(f"calling initializer for {self}")
        self.name = name
        self.id = roll


    def study(self):
        print(self)
        print("Hello there!")


s1 = Student("carel", 188)

s2 = Student("john", 1003)
print(s1.__dict__)
print(help(Student))

print(s1.college_name)
print(s1.department)
print(Student.department)
print(Student.college_name)
