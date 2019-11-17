from decimal import Decimal
from fractions import Fraction

from number.NumberType import NumberType


class NumberFabric:

    def createNumberFromType(self, numberType, nominator, denominator):
        if numberType == NumberType.DECIMAL:
            return Decimal(Decimal(nominator) / Decimal(denominator))
        elif numberType == NumberType.FLOAT:
            return nominator / denominator
        elif numberType == NumberType.FRACTION:
            return Fraction(nominator, denominator)
        else:
            raise Exception
