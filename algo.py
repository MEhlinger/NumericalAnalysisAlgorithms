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


def secantMethod(g,p0,p1, tol, maxIterations):
    outputString = ""
    p = 0
    i = 2
    q0 = util.substituteXAndEval(g,p0)
    q1 = util.substituteXAndEval(g,p1)
    notFirstIteration = False
    while (abs(p - p1) > tol):
        if notFirstIteration:
            p1 = p
        p =  p1 - ((q1 * (p1-p0))/(q1-q0))
        lineOutput = "p{}:{}\n".format(i,p0)
        i += 1
        p0 = p1
        q0 = q1
        q1 = util.substituteXAndEval(g, p)
        outputString += lineOutput
        notFirstIteration = True
        if i > maxIterations:
            return "Max Iterations ({}) reached, method\
            failed.".format(maxIterations)
    outputString += ">>> p={}\n".format(p)
    return outputString
