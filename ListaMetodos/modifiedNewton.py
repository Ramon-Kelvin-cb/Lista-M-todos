import math as math

def derivative(function, value):
    return (function(value + 10**(-5)) - function(value))/(10**(-5))

def modifiedNewton(function, interval, precision):
    x0 = interval[0]
    x1 = interval[1]
    initialGuess = (x0 + x1)/2
    fixedSlope = derivative(function, initialGuess)

    if abs(function(initialGuess)) < precision:
        return initialGuess

    next = initialGuess - function(initialGuess)/fixedSlope

    while abs(function(next)) > precision:
        if abs(next - initialGuess) < precision:
            return next

        initialGuess = next
        next = initialGuess - function(initialGuess)/fixedSlope

    return next
