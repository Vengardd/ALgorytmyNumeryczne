from number.Number import Number
from fractions import Fraction

class FractionNumber(Number):

    value = 0

    def __init__(self, numerator=0, denominator=0):
        self.value = Fraction(numerator, denominator)

    def add(self, other):
        pass

    def substract(self, other):
        pass

    def multiply(self, other):
        pass

    def divide(self, other):
        pass

    def print(self):
        print("Fraction")