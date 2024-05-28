import rootIsolation as ri
import bissection as bi
import math as math

testfunction = lambda x: x + math.log(x)
intervals = ri.rootIntervalFinding(0, 10, testfunction)

if intervals is not None:
    for interval in intervals:
        approx = bi.bissection(testfunction, interval, 0.000001)
        print(f'There ia a root in this interval: {interval}')
        print(f'The root is approx.: {approx}\n')
