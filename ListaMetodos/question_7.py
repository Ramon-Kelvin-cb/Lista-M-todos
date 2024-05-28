import rootIsolation as ri
import math as math

print(ri.rootIntervalFinding(0,10, lambda x: math.sqrt(x) - 5 * math.e ** (- x)))
print(ri.rootIntervalFinding(-10,10, lambda x: x ** 3 - 9 * x + 3))
