from number.Number import Number
from fractions import Fraction


class FractionNumber(Number):
    value = Fraction(0,1)

    def __init__(self, numerator=0, denominator=1):
        self.value = Fraction(numerator, denominator)

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value

    def __str__(self) -> str:
        return self.value.numerator / self.value.denominator

    def print(self):
        print("Fraction")