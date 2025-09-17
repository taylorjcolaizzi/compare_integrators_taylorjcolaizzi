# Compare different quadrature rules for integration

There are two examples provided for calculating the weights and abscissas for gaussian quadrature rules, try:

```
make
./gqconstants
```

or

```
python gqconstants.py
```

You can also use the C++ example as a guide to build your own executable

There is no need to look at rules >~25 for Gaussian quadrature.  And you can also stop at ~ 1000 divisions for the trapezoidal and Simpson's rules.  If you run much longer you'll see the numerical errors bevome visible for the trapezoidal, but you'll need to think about how to code efficiently or the running time may be very long.

Question 1

You can just look at my code named integrators.py. There, I've defined several functions that take care of this. However, you can clearly see that I haven't got a Gaussian quadrature function. That is because I ran out of time.

Question 2

I have a print out that runs when you type into the console the following command:

python integrators.py

Question 3

You can look at my plot Errors.png to see how I've graphed the log-log of relative error versus N.

Question 4

To get the slopes, I just did elementary slope formula. This is equivalent to alpha in Landau's power law equation.

For the algorithmic region, the slopes are
trapezoid  = -1.01
simpson = -3.89
gauss = 0 since I don't have any function here.

I unfortunately didn't have time to calculate this for the round-off region.

Now, moving on to the questions from Canvas.

The function that I wanted to test was sin(100x). I did look up on Google which functions are hard to integrate numerically, and it suggested a function that was highly varying. So, I picked one that's easy to integrate by hand using the chain rule.

Since I don't have Gaussian quadrature in my code, I didn't get to test that. But, you can see that for small numbers of divisions, the errors for trapezoid and simpson rule are very high compared to the exponential function. I suspect that these errors are a manifestation of the Nyquist-Shannon sampling theorem. Since the number of subdivisions per period is less than 2 for N less than 200, aliasing occurs! In that case, the sampling points don't have enough information about the high frequency oscillation that they can't accurately map to the function. Thus, the integral based on those points also fails for the same reason.

To solve this problem, I would recommend doing a substitution that "slows down" the function so that it's easier to integrate with fewer subdivisions. For example, making the substitution y = x / 200 takes the function from sin(100x) to sin(y/2). Since the frequency is less than 1, you don't have to worry about the Nyquist-Shannon theorem if you use any number of points greater than or equal to 3, for example.

Out of time!