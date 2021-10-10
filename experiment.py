from fractions import Fraction # use rational numbers, they are more precise than floats
e = Fraction(0)
f = Fraction(1)
n = Fraction(1)
while True:
    d = Fraction(1) / f # this ...
    if d < Fraction(1, 10**40): # don't continue if the advancement is too small
        break
    e += d # ... and this are the formula you wrote for "e"
    f *= n # calculate factorial incrementally, faster than calling "factorial()" all the time
    n += Fraction(1) # we will use this for calculating the next factorial
print(float(e))