import numpy as np
import matplotlib.pyplot as plt
from math import exp
from math import sin
from math import log10
from math import cos
from gqconstants import HighPrecisionGaussInt

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
        points = int(points / 2 + .5)
        sum = 0.
        width = maximum - minimum
        h = width / points
        hthird = h / 3
        for i in range(points):
            x = minimum + i * h; # where we evaluate function
            # sum += hthird * ( function(x) + 2 * function(x + h) * (i%2) + 2 * function(x + h) + function(x + h + h) )
            sum += hthird * ( function(x) + 4 * function(x + h/2) + function(x + h) ) / 2

            # Originally I was double counting. Not sure how best to get rid of double counting without just dividing 2????
        return sum
            


# gaussian quadrature ~~~~~~~~~~~~~~~~~~~
def gauss(function, points, minimum, maximum):
    """
    I got no idea how to do this currently. will come back and fix...
    currently, it just does nothing but return 0.

    Maybe will implement with the gaussian quadrature in the gqconstants, but I don't know how that works yet...
    """
    return 0

# running ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def neg_exp(x):
    """
    takes in point. negates it. plugs into exp from math
    """
    return exp(-1 * x)

def fast_sin(x):
    """
    takes in point. multiplies by 100. calculates sin
    """
    # return sin(100 * x)
    return sin(100 * x)

def integral_exp():
    """
    integral of e^(-x) from 0 to 1 is
    1 - e^(-1)
    """
    return 1 - exp(-1)

def integral_sin():
    """
    integral of sin(100 * x) from 0 to 1 is
    -.01cos(100 * x)
    """
    return (-0.01 * cos(100 * 1)) - (-0.01 * cos(100 * 0))

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

spacings = [3, 11, 21, 41, 81, 161, 251, 581, 999, 2001, 5003, 100005]
integrals = [integral_exp, integral_sin]
minimum = 0.
maximum = 1.
# printing it out
print("here is part 2 of the assignment for the following N values")
print("---------------")
print("N, e_T, e_S, e_G")
print("---------------")
for n in spacings:
    print(
        n,
        error(trapezoid(neg_exp, n, minimum, maximum), integral_exp()),
        error(simpson(neg_exp, n, minimum, maximum), integral_exp()),
        error(gauss(neg_exp, n, minimum, maximum), integral_exp())
    )

# making log log plot of relative error versus N ~~~~~~~
methods = [trapezoid, simpson, gauss]
functions = [neg_exp]
# so here's the plotting. the method loop is from copilot with some name tweaks from me
print('plotting and saving problem 3')
print("-------------------")
fig, axes = plt.subplots(1, 1, figsize = (10, 8))
plt.suptitle("Plotting log-log Relative Error versus N")
for i, func in enumerate(functions):
    for method in methods:
        now_error = [error(method(func, n, minimum, maximum), integral_exp()) for n in spacings]
        axes.plot((spacings), (now_error), label = method.__name__, marker = 'o')
        axes.set_ylabel("log of abs(error)")
        axes.set_xlabel("log of N")
        axes.set_title("integrate exp(-x)")
        # axes.set_title("integrate sin(100x)")
        axes.legend()
        axes.set_xscale('log')
        axes.set_yscale('log')
        axes.grid()

        print(method.__name__, "yields slope", (log10(now_error[6]) - log10(now_error[1])) / (log10(spacings[6]) - log10(spacings[1])))

plt.tight_layout()
plt.savefig("Errors.png")
# print('plot done bruh')
plt.show()


# doing a tricky function sin(100x)

# this will be tricky because you have fast oscillations. Need lots of steps here to work well.

print('plotting for bad function sin(100x)')
functions = [fast_sin]
fig, axes = plt.subplots(1, 1, figsize = (10, 8))
plt.suptitle("Plotting log-log Relative Error versus N")
for i, func in enumerate(functions):
    for method in methods:
        now_error = [error(method(func, n, minimum, maximum), integral_sin()) for n in spacings]
        axes.plot((spacings), (now_error), label = method.__name__, marker = 'o')
        axes.set_ylabel("log of abs(error)")
        axes.set_xlabel("log of N")
        # axes.set_title("integrate exp(-x)")
        axes.set_title("integrate sin(100x)")
        axes.legend()
        axes.set_xscale('log')
        axes.set_yscale('log')
        axes.grid()

plt.tight_layout()
plt.savefig("BadErrors.png")
# print('plot done bruh')
plt.show()