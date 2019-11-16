from number.Number import Number
from decimal import *

class DecimalNumber(Number):

    value = Decimal(0)

    def __init__(self, numerator=0, denominator=1):
        self.value = Decimal(numerator) / Decimal(denominator)

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv__(self, other):
        return self.value / other.value


    def print(self):
        print("decimal")