from abc import ABC, abstractmethod
class Number(ABC):

    def print(self):
        pass

    @abstractmethod
    def add(self, other):
        pass
    @abstractmethod
    def substract(self, other):
        pass
    @abstractmethod
    def multiply(self, other):
        pass
    @abstractmethod
    def divide(self, other):
        pass