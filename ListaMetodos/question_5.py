import math as math

def recurrency(i):
    if i == 0:
        return 1
    if i == 1:
        return 1/3

    return (13/3)*recurrency(i - 1) - (4/3)*recurrency(i - 2)

realValues = []
computedValues = []

for i in range(20):
    realValues.append((1/3)**i)
    computedValues.append(recurrency(i))

comparisson = [] #Absolute error
print(realValues)
print(computedValues)

for i, value in enumerate(realValues):
    comparisson.append(abs(value - computedValues[i]))

print(comparisson)
