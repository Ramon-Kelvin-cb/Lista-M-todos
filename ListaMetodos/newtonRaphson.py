import math as math

def derivative(function, value):
    return (function(value + 10**(-5)) - function(value))/(10**(-5))

def applyApprox(value, function):
    return value - function(value)/derivative(function, value)

def newtonRaphson(function, interval, precision):
    initialGuess = (interval[0] + interval[1])/2
    next = applyApprox(initialGuess, function)

    if abs(function(initialGuess)) < precision:
        return initialGuess

    while abs(next - initialGuess) > precision:
        if abs(function(initialGuess)) < precision or abs(next - initialGuess) < precision:
            return next

        initialGuess = next
        next = applyApprox(initialGuess, function)

    return next
