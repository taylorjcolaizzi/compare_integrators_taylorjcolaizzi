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

To get the slopes, I just did elementary slope formula.

For the algorithmic region, the slopes are
trapezoid  = -1.01
simpson = -3.89
gauss = 0 since I don't have any function here.

And in the round-off region,
