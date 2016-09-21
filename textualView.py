#!/usr/bin/env python3

import algo, sys, util

class Menu:

    def __init__(self):
        self.menuItems = [
                "Newton-Raphson",
                "Secant",
                "Newton Mod 1",
                "Newton Mod 2",
                "Quit"
            ]

    def display(self):
        while True:
            print('''
                ---------------------
                 NumbAnal Algorithms
                ---------------------
                by Marshall Ehlinger
                for Numerical 
                Analysis FA 2016
                ---------------------
    
                ''')
            for menuItem in self.menuItems:
                print(">> " + menuItem)
            self.processInput()
    
    def processInput(self):
        choice = input("\nEnter your choice -exactly- as in menu  and press RETURN: \n")
        if choice == "Newton-Raphson":
            print(">> You have selected Netwon-Raphson.")
            if input("Press 'y', then RETURN if correct.") == "y":
                f = input("Enter function 'f(x)' as valid Python expression: ")
                fprime = input("Enter f'(x) as valid Python expression: ")
                p0 = float(input("Enter initial estimate: "))
                tol = float(input("Enter tolerance for answer: "))
                maxIterations = float(input("Enter maximum iterations before giving up: "))
                outputFilename = input("Enter Output Filename: ")
                util.printAndWriteStringToFile(algo.newtonRaphson(f, fprime, p0, tol,
                    maxIterations), outputFilename)
            else:
                return
        elif choice == "Newton Mod 1":
            print(">> You have selected Netwon-Raphson Modification 1.")
            if input("Press 'y', then RETURN if correct.") == "y":
                f = input("Enter function 'f(x)' as valid Python expression, using 'x' as the single variable: ")
                fprime = input("Enter derivative of f(x) as valid Python expression, using 'x' as the single variable: ")
                p0 = float(input("Enter inital guess: "))
                tol = float(input("Enter tolerance for answer: "))
                maxIterations = float(input("Enter maximum iterations before giving up: "))
                m = int(input("Enter multiplicity as integer:"))
                outputFilename = input("Enter Output Filename: ")
                util.printAndWriteStringToFile(algo.newtonRaphsonMod1(f,
                    fprime, p0, tol, maxIterations, m), outputFilename)
            else:
                return
        elif choice == "Newton Mod 2":
            print(">> You have selected Netwon-Raphson Modification 2.")
            if input("Press 'y', then RETURN if correct.") == "y":
                f = input("Enter f(x): ")
                fprime = input("Enter f'(x): ")
                fdoubleprime = input("Enter f''(x): ")
                p0 = float(input("Enter inital estimate: "))
                tol = float(input("Enter tolerance: "))
                maxIterations = float(input("Enter maximum iterations: "))
                outputFilename = input("Enter output filename: ")
                util.printAndWriteStringToFile(algo.newtonRaphsonMod2(f,
                    fprime, fdoubleprime, p0, tol, maxIterations),
                    outputFilename)
            else:
                return
        elif choice == "Secant":
            print(">> You have selected the Secant Method.")
            if input("Press 'y', then RETURN if correct.") == "y":
                g = input("Enter function 'g(x)' as valid Python: ")
                x0 = float(input("Enter x0: "))
                x1 = float(input("Enter x1: "))
                tol = float(input("Enter tolerance: "))
                maxIterations = float(input("Enter maximum iterations: "))
                outputFilename = input("Enter output filename: ")
                util.printAndWriteStringToFile(algo.secantMethod(g,x0,x1,tol,maxIterations),
                        outputFilename)
            else:
                return
        elif choice == "Quit":
            print("Goodbye.\n\n")
            sys.exit() 


