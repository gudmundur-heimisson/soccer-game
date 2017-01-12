from math import pow, floor, sqrt

def y(t, c1, c2, c3):
    return c1 * pow(t,2) + c2 * t + c3 

def y_inv(y, c1, c2, c3):
    return (-c2 - sqrt(pow(c2, 2) - 4 * c1 * (c3-y))) / (2 * c1)

def X(t, c1, c2):
    return c1 * t + c2 

def x(t, c1, c2):
    Xf = X(t, c1, c2)
    Xl = floor(Xf)
    return pow(-1, Xl) * (Xf - Xl - 0.5) + 0.5

