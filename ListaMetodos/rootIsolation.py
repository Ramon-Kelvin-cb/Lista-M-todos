import numpy as np
import math

def partitioner(start, stop, slices):
    stepSubdivision = np.arange(0.000001, 1, 1/slices) #Open intervals only
    return [start + (stop - start) * x for x in stepSubdivision]

def signalAtPoint(domainValues, function):
    return ["+" if function(x) > 0 else "-" for x in domainValues]

def rootIntervalFinding(start, stop, function):
    try:
        domainInterval = partitioner(start, stop, 37)
        signalCheck = "+" if function(domainInterval[0]) > 0 else "-"

        rootIntervals = []
        for i, element in enumerate(signalAtPoint(domainInterval, function)):
            if element == signalCheck :
                continue
            else:
                rootIntervals.append([domainInterval[i - 1], domainInterval[i]])
                signalCheck = element
        return rootIntervals

    except ValueError:
        print("There's a error in the domain, try changing it by analyzing the domain")
