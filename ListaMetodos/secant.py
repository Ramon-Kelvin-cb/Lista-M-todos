import math as math

def secant(function, interval, precision):
    x0 = interval[0]
    x1 = interval[1]

    if abs(function(x0)) < precision:
        return x0

    while abs(x1 - x0) > precision:
        if abs(function(x1)) < precision:
            return x1

        x2 = x1 - (x1 -x0)*function(x1)/(function(x1) - function(x0))

        if abs(function(x2)) < precision or abs(function(x2) - function(x1)) < precision:
            return x2

        x0 = x1
        x1 = x2
