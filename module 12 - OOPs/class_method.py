# Any method created in class are  called as instance method
"""
Class methods are methods defined inside the class that are bound to the class
To create a class method , we use a decorator -> class method
"""


class Welcome:

    @classmethod
    def greet(cls):
        print(cls)
        print("Hello")


w1 = Welcome()
w1.greet()
print(Welcome)
print("---------------------------------------------------")


class Student:
    college_name = "sree dattha institutions"
    department = ["CSE", "EEE", "CSBS", "AIML"]

    def __init__(self, name, roll):
        # print(f"calling initializer for {self}")
        self.hours = None
        self.name = name
        self.id = roll

    def study(self, hours):
        self.hours = hours
        print(self)
        print(f"Hello {self.name}, how many hours you play? {hours} in college {self.college_name}")

    @classmethod
    def inviting(cls):
        print(cls)
        print(f"welcome to {cls.college_name}, departments we have:")
        for depart in cls.department:
          print(f"{depart}")


s1 = Student("carel", 188)

s2 = Student("john", 1003)
s1.study(3)
s2.study(2)
s1.inviting()
