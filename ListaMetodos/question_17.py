import rootIsolation as ri
import bissection as bi
import math as math

testfunction = lambda x: ((8*x)/(math.sqrt(900 - x**2))) + ((8*x)/(math.sqrt(400 - x**2))) - x
intervals = ri.rootIntervalFinding(-20, 20, testfunction)

if intervals is not None:
    for interval in intervals:
        approx = bi.bissection(testfunction, interval, 0.000001)
        print(f'There ia a root in this interval: {interval}')
        print(f'The root is approx.: {approx}\n')
