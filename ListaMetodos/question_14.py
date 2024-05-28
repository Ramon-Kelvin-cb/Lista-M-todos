import math as math
import rootIsolation as ri

def iteration_14(value):
    return 1/value + 1/(value)**2

def fixedPoint_14(precision):
    initialGuess = 1
    function = lambda x: x**3 - x - 1
    if abs(function(initialGuess)) < precision:
        return initialGuess

    next = iteration_14(initialGuess)

    while abs(function(next)) > precision:
        print(next)
        if abs(next - initialGuess) < precision:
            return next

        initialGuess = next
        next = iteration_14(initialGuess)

    return next

# QUESTÃO 14 -> A FUNÇÃO SAI DO INTERVALO DE CONVERGÊNCIA DEVIDO À FUNÇÃO DE ITERAÇÃO NÃO POSSUIR DERIVADA LIMITADA
function_14 = lambda x: x**3 - x - 1
intervals = ri.rootIntervalFinding(-10, 10, function_14)

print(intervals)
approx = fixedPoint_14(0.00001)
