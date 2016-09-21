#!/usr/bin/env python3

import util


def newtonRaphson(f, fprime, p0, tol, maxIterations):
    outputString = ""
    p = 0
    i = 0
    notFirstIteration = False
    while (abs(p - p0) > tol):
        if notFirstIteration:
            p0 = p
        p =  p0 - util.substituteXAndEval(f,p0) / util.substituteXAndEval(fprime,p0)
        i += 1
        lineOutput = "i:{}, p:{}, p0:{}\n".format(i, p, p0)
        outputString += lineOutput
        notFirstIteration = True
        if i > maxIterations:
            return "Max Iterations ({}) reached, method\
            failed.".format(maxIterations)
    print("Newton-Raphson succeeded on {}th iteration.".format(i))
    outputString += ">>> p={}\n".format(p)
    return outputString
        
def newtonRaphsonMod1(f, fprime, p0, tol, maxIterations, m): 
    outputString = ""
    p = 0
    i = 0
    notFirstIteration = False
    while (abs(p - p0) > tol):
        if notFirstIteration:
            p0 = p
        p =  p0 - (m * util.util.substituteXAndEval(f,p0) / util.substituteXAndEval(fprime,p0))
        i += 1
        lineoutput = "i:{}, p:{}, p0:{}\n".format(i, p, p0)
        outputString += lineOutput
        notFirstIteration = True
        if i > maxIterations:
            return "Max Iterations ({}) reached, method failed.".format(maxIterations)
    print("Newton-Raphson succeeded on {}th iteration.".format(i))
    outputString += ">>> p={}\n".format(p)
    return outputString


def newtonRaphsonMod2(f, fPrime, fDoublePrime, p0, tol, maxIterations):
    outputString = ""
    p = 0
    i = 0
    notFirstIteration = False
    while (abs(p - p0) > tol):
        if notFirstIteration:
            p0 = p
        if (util.util.substituteXAndEval(fPrime,p0)**2 - util.substituteXAndEval(f,p0) * util.substituteXAndEval(fDoublePrime, p0)) == 0:
            return "Attempted divison by 0. Not valid."
        p =  p0 - (util.util.substituteXAndEval(f,p0) * util.substituteXAndEval(fPrime, p0)) / (util.substituteXAndEval(fPrime,p0)**2 - util.substituteXAndEval(f,p0) * util.substituteXAndEval(fDoublePrime, p0))
        i += 1
        lineoutput = "i:{}, p:{}, p0:{}\n".format(i, p, p0)
        outputString += lineOutput
        notFirstIteration = True
        if i > maxIterations:
            return "Max Iterations ({}) reached, method\
            failed.".format(maxIterations)
    outputString += ">>> p={}\n".format(p)
    return outputString
