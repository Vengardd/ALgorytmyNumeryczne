from FloatNumber import FloatNumber
from NumberFabric import NumberFabric
from NumberType import NumberType

print("test")

fabric = NumberFabric()
numberType = NumberType.FLOAT
number = fabric.createNumberFromType(numberType)
number.print()
