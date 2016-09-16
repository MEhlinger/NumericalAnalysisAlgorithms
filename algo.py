#!/usr/bin/env python3

def substituteXAndEval(functionString, x):
    return eval(functionString.replace("x", str(x)))

def newtonRaphson(f, fprime, lo, hi, tol, maxIterations):
    # initial estimate
    p0 = hi - lo
    p = 0
    i = 0
    while (abs(p - p0) > tol):
        if p != 0: 
            p0 = p
        p =  p0 - substituteXAndEval(f,p0) / substituteXAndEval(fprime,p0)
        i += 1
        print("p: " + str(p) + ", p0: " + str(p0))
        if i > maxIterations:
            return "Max Iterations ({}) reached, method\
            failed.".format(maxIterations)
    print("Newton-Raphson succeeded on {}th iteration.".format(i))
    return p
        
