import FractionNumber
from DecimalNumber import DecimalNumber
from FloatNumber import FloatNumber
from NumberType import NumberType

class NumberFabric:

    def createNumberFromType(self, numberType):
        if numberType == NumberType.DECIMAL:
            return DecimalNumber
        elif numberType == NumberType.FLOAT:
            return FloatNumber()
        elif numberType == NumberType.FRACTION:
            return FractionNumber.FractionNumber
        else:
            raise Exception
