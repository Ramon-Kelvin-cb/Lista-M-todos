import math as math

def sumBackwards(list):
    size = len(list)
    sum = 0

    for i in range(0,size):
        sum += list[-i]

    return sum

def nthTerm(n):
    return ((-1)**n)*(4/(2*n + 1))

sum = 0
values = []
i = 0

currentTerm = nthTerm(i)
values.append(currentTerm)

while abs(currentTerm) > 0.00001:
    sum += currentTerm
    i += 1
    currentTerm = nthTerm(i)
    values.append(currentTerm)

print(sum)
print(sumBackwards(values))
