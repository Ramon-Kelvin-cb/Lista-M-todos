import math as math
import bissection as bi
import newtonRaphson as nw
import rootIsolation as ri

def combined(function, interval):
    initialGuess = bi.bissection(function, interval, 10**(-2))
    return nw.newtonRaphson(function,[initialGuess - 0.005, initialGuess + 0.005] ,10**(-7))

testfunction = lambda x: x**3 - 3.5*x**2 + 4*x - 1.5
intervals = ri.rootIntervalFinding(-10, 10, testfunction)

if intervals is not None:
    for interval in intervals:
        approx = combined(testfunction, interval)
        print(f'There ia a root in this interval: {interval}')
        print(f'The root is approx.: {approx}\n')
