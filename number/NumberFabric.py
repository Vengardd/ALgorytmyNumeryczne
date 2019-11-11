from number.FractionNumber import FractionNumber
from number.DecimalNumber import DecimalNumber
from number.FloatNumber import FloatNumber
from number.NumberType import NumberType

class NumberFabric:

    def createNumberFromType(self, numberType, nominator, denominator):
        if numberType == NumberType.DECIMAL:
            return DecimalNumber(nominator, denominator)
        elif numberType == NumberType.FLOAT:
            return FloatNumber(nominator, denominator)
        elif numberType == NumberType.FRACTION:
            return FractionNumber(nominator, denominator)
        else:
            raise Exception
