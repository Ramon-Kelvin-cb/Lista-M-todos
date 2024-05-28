import math as math

def falsePosition(function, interval, precision):
    a = interval[0]
    b = interval[1]

    if abs(function(a)) < precision:
                return a

    if abs(function(b)) < precision:
                return b

    while b - a > precision:
        guess = (a * function(b) - b * function(a))/(function(b) - function(a))

        if a < 0 < b and function(0) == 0:
            return 0

        if abs(function(guess)) < precision:
            return guess

        if function(a) * function(guess) < 0:
            b = guess
        else:
            a = guess

    return (a + b)/2
