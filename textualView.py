#!/usr/bin/env python3

import algo, sys

class Menu:

    def __init__(self):
        self.menuItems = [
                "Newton-Raphson",
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
            print(".")
            self.processInput()
        print("Goodbye.\n\n")
    
    def processInput(self):
        choice = input("\nEnter your choice -exactly- as in menu  and press RETURN: \n")
        if choice == "Newton-Raphson":
            print(">> You have selected Netwon-Raphson.")
            if input("Press 'y', then RETURN if correct.") == "y":
                f = input("Enter function 'f(x)' as valid Python expression, using 'x' as the single variable: ")
                fprime = input("Enter derivative of f(x) as valid Python expression, using 'x' as the single variable: ")
                lo = float(input("Enter lower bound of region: "))
                hi = float(input("Enter higher bound of region: "))
                tol = float(input("Enter tolerance for answer: "))
                maxIterations = float(input("Enter maximum iterations before giving up: "))
                print(algo.newtonRaphson(f, fprime, lo, hi, tol,
                    maxIterations))
            else:
                return
        elif choice == "Quit":
            sys.exit() 


if __name__ == "__main__":
    menu = Menu()
    menu.display()
