#!/usr/bin/env python3

# Utility functions for Numerical Analysis Algorithm Calculator
# 9/20/16 Marshall Ehlinger

import datetime, math

def substituteXAndEval(functionString, x):
    return eval(functionString.replace("x", str(x)))

def printAndWriteStringToFile(string, outputFilename):
    print(string)
    f = open(outputFilename, 'w')
    f.write(string)
    f.close
