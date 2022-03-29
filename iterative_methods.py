from math import *
def simple_iteration(function, initial_guess, stopping_criteria = 0.000005):

    f_of_initial_guess = eval(function)
    answer = 0
    n = 1
    stopping_criteria_check = 1
    while stopping_criteria_check > stopping_criteria:
        stopping_criteria_check = abs(f_of_initial_guess - answer)
        answer = f_of_initial_guess
        function2 = function.replace(str(initial_guess), str(answer))
        f_of_initial_guess = eval(function2)
        print(f"x{n} = {f_of_initial_guess}")
        n += 1
    print(f"Iteration converges at x{n} = {f_of_initial_guess}")


"""simple_iteration("cos x", 0.7)"""


def bisection_method(function1, function2,
                    first_initial_guess, 
                    second_initial_guess, 
                    stopping_criteria = 0.000005):
    f_of_first_initial_guess = eval(function1)
    f_of_second_initial_guess = eval(function2)
    print(f"x1 = {f_of_first_initial_guess}")
    print(f"x2 = {f_of_second_initial_guess}")
    stopping_criteria_checker = abs(float(second_initial_guess) - float(first_initial_guess))
    n = 2
    third_guess = 0
    while stopping_criteria_checker > stopping_criteria:
        third_guess = (float(first_initial_guess) + float(second_initial_guess))/2
        function3 = function1.replace(str(first_initial_guess), str(third_guess))
        f_of_third_guess = eval(function3)
        if f_of_third_guess < 0:
            first_initial_guess = third_guess
        else:
            second_initial_guess = third_guess
        stopping_criteria_checker = abs(float(second_initial_guess) - float(first_initial_guess))
        print(f"x{n} = {third_guess}")
        n += 1
    print(f"Answer is {third_guess}")

"""bisection_method("x - cosx", 0, pi/2)"""


"""def newton_raphson_method(function, initial_guess, stopping_criteria = 0.000005):
    f_of_initial_guess = eval(function)
    dervative_function
    n = 1
    guesses = 0
    stopping_criteria_checker = 1
    while stopping_criteria_checker > stopping_criteria:
        pass
    """


#function for secant method
def secant_method(function0, function1, initial_guess, initial_guess1, stopping_criteria = 0.000005):
    f_of_initial_guess = eval(function0)
    f_of_initial_guess1 = eval(function1)
    print(f"f({initial_guess}) = {f_of_initial_guess}")
    print(f"f({initial_guess1}) = {f_of_initial_guess1}")
    n = 2
    third_guess = 0
    stopping_criteria_checker = 1
    while stopping_criteria_checker > stopping_criteria:
        try:
            third_guess = (float(initial_guess1) * f_of_initial_guess - float(initial_guess) * f_of_initial_guess1) / (f_of_initial_guess1 - f_of_initial_guess)
        except ZeroDivisionError:
            break

        function3 = function0.replace(str(initial_guess), str(third_guess))
        function3 = eval(function3)
        print(f"f({third_guess}) = {function3}")
        stopping_criteria_checker = abs(float(initial_guess1) - float(initial_guess))
        initial_guess = initial_guess1
        initial_guess1 = third_guess

        f_of_initial_guess = f_of_initial_guess1
        f_of_initial_guess1 = function3


        print(f"x{n} = {third_guess}")
        n += 1
    print(f"It coverges at {third_guess}")

"""secant_method(cosx, cosx, 0.8, 0.6)"""

def regular_falsi_method(function1, 
                        function2, 
                        first_initial_guess, 
                        second_initial_guess, 
                        stopping_criteria = 0.000005):
    #Making sure the unknown is expressed in terms of x and replacing the x with initial guesses.
    #Am assuming that other alphabets will be used for trig functions or any other function
    f_of_first_initial_guess = eval(function1)
    f_of_second_initial_guess = eval(function2)
    n = 2
    checker = 0
    third_guess = 0
    stopping_criteria_checker = 1
    while stopping_criteria_checker > stopping_criteria:
        try:
            third_guess = float(first_initial_guess) - ((float(first_initial_guess) - float(second_initial_guess)) * (f_of_first_initial_guess)
                                        /(f_of_first_initial_guess - f_of_second_initial_guess))
        except ZeroDivisionError:
            break
        if third_guess > float(first_initial_guess):
            first_initial_guess = third_guess
        else:
            second_initial_guess = third_guess
        function3 = function1.replace(first_initial_guess, str(third_guess))
        f_of_third_guess = eval(function3)
        stopping_criteria_checker = abs(third_guess - checker)
        checker = third_guess
        print(f"x{n} = {third_guess}")
        n += 1
    print(f"It converges at {(third_guess)}")
    