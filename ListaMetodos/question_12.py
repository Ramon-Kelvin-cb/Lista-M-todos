import math as math
import bissection as bi
import falsePosition as fp
import newtonRaphson as nw
import secant as sc
import fixedPoint as fx

function1 = lambda x: x**3 - x - 1
function2 = lambda x: math.e ** (- x**2) - math.cos(x)

interval = [1,2]
bissection1 = bi.bissection(function1, interval, 10**(-6))
bissection2 = bi.bissection(function2, interval, 10**(-4))

falsePosition1 = fp.falsePosition(function1, interval, 10**(-6))
falsePosition2 = fp.falsePosition(function2, interval, 10**(-4))

newton1 = nw.newtonRaphson(function1, interval, 10**(-6))
newton2 = nw.newtonRaphson(function2, interval, 10**(-4))

secant1 = sc.secant(function1, interval, 10**(-6))
secant2 = sc.secant(function2, interval, 10**(-4))

fixedPoint1 = fx.fixedPoint(function1, lambda x: math.pow(x + 1, 1/3), interval, 10**(-6))
fixedPoint2 = fx.fixedPoint(function2, lambda x: math.acos(math.pow(math.e, -x**2)), interval, 10**(-4))

print("Using bissection:")
print(bissection1)
print(bissection2)
print("")
print("Using false position:")
print(falsePosition1)
print(falsePosition2)
print("")
print("Using Newton Raphson:")
print(newton1)
print(newton2)
print("")
print("Using Secant:")
print(secant1)
print(secant2)
print("")
print("Using Fixed Point:")
print(fixedPoint1)
print(fixedPoint2)
print("")
