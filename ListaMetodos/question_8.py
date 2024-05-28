import bissection as bi
import rootIsolation as ri

testfunction = lambda x: x**3 - 9*x + 3
intervals = ri.rootIntervalFinding(-10, 10, testfunction)

if intervals is not None:
    for interval in intervals:
        approx = bi.bissection(testfunction, interval, 0.000001)
        print(f'There ia a root in this interval: {interval}')
        print(f'The root is approx.: {approx}\n')
