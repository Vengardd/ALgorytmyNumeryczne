from number.FloatNumber import FloatNumber
from number.NumberFabric import NumberFabric
from number.NumberType import NumberType

print("test")

fabric = NumberFabric()
numberType = NumberType.FLOAT
number = fabric.createNumberFromType(numberType, 5, 1)
number.print()
number.add(FloatNumber(10, 2))
print(number.value)
