import numpy as np
import matplotlib.pyplot as plt
from math import exp

# trapezoid rule ~~~~~~~~~~~~~~~~~~~~~~~~
def trapezoid(function, points, minimum, maximum, verbose = 0):
    """
    takes 1-d function to be integrated from minimum to 
    maximum. points is number of subdivisions to step over.
    uses trapezoid rule, which is just reimann sum using
    a trapezoid shape instead of rectangle
    """

    sum = 0. # total integral
    width = maximum - minimum
    h = width / points

    for i in range(points):
        x = minimum + (i * h)
        if i == 0 or i == (points - 1):
            sum += function(x) * h / 2
        else:
            sum += function(x) * h
    if verbose == 1:
        print("sum is", sum)
    return sum

# simpson rule ~~~~~~~~~~~~~~~~~~~~~~~~~~
def simpson(function, points, minimum, maximum):
    """
    same as trapezoid, but it uses simpson rule.
    REQUIRES ODD points TO FUNCTION CORRECTLY

    simpson rule is like reimann sum but we use parabolas
    and weight them to points inside versus edge
    """
    if points % 2 != 1:
        print("Simpson's rule needs odd number of points to work correctly")
        return 1
    else:
        sum = 0.
        width = maximum - minimum
        h = width / points
        hthird = h / 3
        for i in range(points):
            x = minimum + i * h; # where we evaluate function
            sum += hthird * ( function(x) + 4 * function(x + h/2) + function(x + h) )
        return sum
            


# gaussian quadrature ~~~~~~~~~~~~~~~~~~~
def gauss(function, points, minimum, maximum):
    """
    I got no idea how to do this currently. will come back and fix...
    currently, it just does nothing.
    """
    return 0

# running ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def neg_exp(x):
    """
    takes in point. negates it. plugs into exp from math
    """
    return exp(-1 * x)

def integral():
    """
    integral of e^(-x) from 0 to 1 is
    1 - e^(-1)
    """
    return 1 - exp(-1)

def error(calculated, actual, absolute = 1):
    """
    takes relative error between calculated and actual values
    """
    if absolute == 1:
        return abs( (calculated - actual) / actual )
    else:
        return (calculated - actual) / actual

# trapezoid(neg_exp, 100, 0, 1)
# print("true value is", 1 - neg_exp(1))

# calculating the error ~~~~~~~~~~~~~~~~~

spacings = [3, 11, 21, 41, 81, 161]
minimum = 0.
maximum = 1.
# printing it out
print("here is part 2 of the assignment for the following N values")
print("N, e_T, e_S, e_G")
for n in spacings:
    print(
        n,
        error(trapezoid(neg_exp, n, minimum, maximum), integral()),
        error(simpson(neg_exp, n, minimum, maximum), integral()),
        error(gauss(neg_exp, n, minimum, maximum), integral())
    )