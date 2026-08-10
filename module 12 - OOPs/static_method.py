"""
Static method -  method defined inside a class which is neither bound to the object nor to the class

"""

class Student:
    college_name = "sree dattha institutions"
    department = ["CSE", "EEE", "CSBS", "AIML"]

    def __init__(self, name, roll):
        print(f"calling initializer for {self}")
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

    @staticmethod
    def greet():
        print("Good morning!!")

student1 = Student("john",89)
student1.greet()