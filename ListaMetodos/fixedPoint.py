import math as math

def fixedPoint(function, iterationFunction, interval, precision):
   initialApprox = (interval[0] + interval[1])/2
   next = iterationFunction(initialApprox)

   if abs(function(initialApprox)) < precision:
       return initialApprox

   while abs(next - initialApprox) > precision:
       if abs(function(next)) < precision or abs(next - initialApprox) < precision:
           return next

       initialGuess = next
       next = iterationFunction(initialGuess)

   return next
