# abc module => Abstract Base Classes
# there is a method called @abstract method

from abc import ABC , abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


