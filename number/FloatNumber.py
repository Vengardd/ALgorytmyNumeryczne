from number.Number import Number

class FloatNumber(Number):

    value = 0

    def __init__(self, numerator=0, denominator=1):
        self.value = numerator / denominator

    def print(self):
        print("float")

    def add(self, other):
        self.value = self.value + other.value

    def substract(self, other):
        self.value = self.value - other.value

    def multiply(self, other):
        self.value = self.value * other.value

    def divide(self, other):
        self.value = self.value / other.value
