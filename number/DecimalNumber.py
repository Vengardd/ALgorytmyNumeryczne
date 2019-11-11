from number.Number import Number
from decimal import *

class DecimalNumber(Number):

    value = 0

    def __init__(self, numerator=0, denominator=1):
        self.value = Decimal(numerator) / Decimal(denominator)

    def add(self, other):
        self.value = Decimal(self.value) + Decimal(other.value)

    def substract(self, other):
        self.value = Decimal(self.value) - Decimal(other.value)

    def multiply(self, other):
        self.value = Decimal(self.value) * Decimal(other.value)

    def divide(self, other):
        self.value = Decimal(self.value) / Decimal(other.value)

    def print(self):
        print("decimal")