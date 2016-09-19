#!/usr/bin/env python3

import math #for use in eval() of user-inputted functions (math.e, for example)

def substituteXAndEval(functionString, x):
    return eval(functionString.replace("x", str(x)))

def newtonRaphson(f, fprime, p0, tol, maxIterations):
    p = 0
    i = 0
    notFirstIteration = False
    while (abs(p - p0) > tol):
        if notFirstIteration:
            p0 = p
        p =  p0 - substituteXAndEval(f,p0) / substituteXAndEval(fprime,p0)
        i += 1
        print("p: " + str(p) + ", p0: " + str(p0))
        notFirstIteration = True
        if i > maxIterations:
            return "Max Iterations ({}) reached, method\
            failed.".format(maxIterations)
    print("Newton-Raphson succeeded on {}th iteration.".format(i))
    return ">>> p={}".format(p)
        
def newtonRaphsonMod1(f, fprime, p0, tol, maxIterations, m): 
    p = 0
    i = 0
    notFirstIteration = False
    while (abs(p - p0) > tol):
        if notFirstIteration:
            p0 = p
        p =  p0 - (m * substituteXAndEval(f,p0) / substituteXAndEval(fprime,p0))
        i += 1
        print("p: " + str(p) + ", p0: " + str(p0))
        notFirstIteration = True
        if i > maxIterations:
            return "Max Iterations ({}) reached, method failed.".format(maxIterations)
    print("Newton-Raphson succeeded on {}th iteration.".format(i))
    return ">>> p={}".format(p)


def newtonRaphsonMod2(f, fPrime, fDoublePrime, p0, tol, maxIterations):
    p = 0
    i = 0
    notFirstIteration = False
    while (abs(p - p0) > tol):
        if notFirstIteration:
            p0 = p
        if (substituteXAndEval(fPrime,p0)**2 - substituteXAndEval(f,p0) * substituteXAndEval(fDoublePrime, p0)) == 0:
            return "Attempted divison by 0. Not valid."
        p =  p0 - (substituteXAndEval(f,p0) * substituteXAndEval(fPrime, p0)) / (substituteXAndEval(fPrime,p0)**2 - substituteXAndEval(f,p0) * substituteXAndEval(fDoublePrime, p0))
        i += 1
        print("p: " + str(p) + ", p0: " + str(p0))
        notFirstIteration = True
        if i > maxIterations:
            return "Max Iterations ({}) reached, method\
            failed.".format(maxIterations)
    print("Newton-Raphson succeeded on {}th iteration.".format(i))
    return ">>> p={}".format(p)
