import math as math

def bissection(function, interval, precision):
    a = interval[0]
    b = interval[1]

    while abs(b - a) > precision:
        middleValue = (b + a)/2

        if a < 0 < b and function(0) == 0:
            return 0

        if function(a) * function(middleValue) > 0:
            a = middleValue
        else:
            b = middleValue

    return (a + b)/2
