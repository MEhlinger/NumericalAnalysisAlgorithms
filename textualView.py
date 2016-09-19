#!/usr/bin/env python3

import algo, sys

class Menu:

    def __init__(self):
        self.menuItems = [
                "Newton-Raphson",
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
        print("Goodbye.\n\n")
    
    def processInput(self):
        choice = input("\nEnter your choice -exactly- as in menu  and press RETURN: \n")
        if choice == "Newton-Raphson":
            print(">> You have selected Netwon-Raphson.")
            if input("Press 'y', then RETURN if correct.") == "y":
                f = input("Enter function 'f(x)' as valid Python expression, using 'x' as the single variable: ")
                fprime = input("Enter derivative of f(x) as valid Python expression, using 'x' as the single variable: ")
                p0 = float(input("Enter initial estimate: "))
                tol = float(input("Enter tolerance for answer: "))
                maxIterations = float(input("Enter maximum iterations before giving up: "))
                print(algo.newtonRaphson(f, fprime, p0, tol,
                    maxIterations))
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
                print(algo.newtonRaphsonMod1(f, fprime, p0, tol, maxIterations, m))
            else:
                return
        elif choice == "Newton Mod 2":
            print(">> You have selected Netwon-Raphson Modification 2.")
            if input("Press 'y', then RETURN if correct.") == "y":
                f = input("Enter function 'f(x)' as valid Python expression, using 'x' as the single variable: ")
                fprime = input("Enter derivative of f(x) as valid Python expression, using 'x' as the single variable: ")
                fdoubleprime = input("Enter second derivative of f(x), using 'x' as the single variable: ")
                p0 = float(input("Enter inital guess: "))
                tol = float(input("Enter tolerance for answer: "))
                maxIterations = float(input("Enter maximum iterations before giving up: "))
                print(algo.newtonRaphsonMod2(f, fprime, fdoubleprime, p0, tol, maxIterations))
            else:
                return
        elif choice == "Quit":
            sys.exit() 


if __name__ == "__main__":
    menu = Menu()
    menu.display()
