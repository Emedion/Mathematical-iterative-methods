from math import *
from sympy import *
from iterative_methods import*
name = input("Enter your name: ")
print(f"Hi {name}, this program will help you carry out iteration using any of the five iterative methods")
while True:
    print("Which iterative method do you want to use?")
    option = input("""Enter: 
                    \n 1 for Simple iteration 
                    \n 2 for Bisection method
                    \n 3 for Secant method
                    \n 4 for Regular Falsi method: """)
    
    function = input("Enter function: ")
    initial_guess = input("Enter initial guess: ")
    function = function.lower()
    
    for i in function:
        if "x^" in function:
            function = function.replace("x^", "(x)**")
        elif "x" in function:
            function = function.replace("x", "(x)")
        else:
            print("Unknown in function must be represented by 'x'.")
        function1 =  function.replace("x", initial_guess)
    
    if option == "1":
        simple_iteration(function1, initial_guess)

    elif option == "2":
        initial_guess2 = input("Enter second initial guess: ")
        for i in function:
            function2 = function.replace("(x)", initial_guess2)
        bisection_method(function1, function2, initial_guess, initial_guess2)



    elif option == "3":
        initial_guess2 = input("Enter second initial guess: ")
        for i in function:
            function2 = function1.replace(initial_guess, initial_guess2)
        secant_method(function1, function2, initial_guess, initial_guess2)

    elif option == "4":
        initial_guess2 = input("Enter second initial guess: ")
        for i in function:
            function2 = function.replace("(x)", initial_guess2)
        if float(initial_guess) > float(initial_guess2):
            regular_falsi_method(function1, function2, initial_guess, initial_guess2)
        else:
            regular_falsi_method(function1, function2, initial_guess2, initial_guess)

    print("Do you want to perform another computation?")
    decision = input("""Enter y for yes
                        \n and n for no: """)
    if decision == "n":
        break
print(f"Bye {name}, till next time")
