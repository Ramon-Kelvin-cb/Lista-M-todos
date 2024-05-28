import rootIsolation as ri
import newtonRaphson as nr
import modifiedNewton as mn
import bissection as bis
import falsePosition as fp
import secant as sc

# testfunction = lambda x: x**3 - 9*x + 3
# intervals = ri.rootIntervalFinding(-10, 10, testfunction)

# if intervals is not None:
#     for interval in intervals:
#         approx = mn.modifiedNewton(testfunction, lambda x: 3*x**2 - 9, interval, 0.000001)
#         print(f'There ia a root in this interval: {interval}')
#         print(f'The root is approx.: {approx}\n')
