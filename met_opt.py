import math


def f(x):
    return math.cos(x)


def dichotomy_method(a, b, eps=1e-4):
    sigma = eps / 2.0
    x = (a + b) / 2.0
    while abs(b - a) > eps:
        x1 = x - sigma
        x2 = x + sigma
        if f(x1) < f(x2):
            b = x1
        elif f(x1) > f(x2):
            a = x2
        else:
            a = x1
            b = x2
        x = (a + b) / 2.0
    return x


def golden_section_method(a, b, eps=1e-4):
    while abs(b - a) > eps:
        x1 = a + 0.381966011 * (b - a)
        x2 = a + 0.618003399 * (b - a)
        if f(x1) < f(x2):
            b = x1
        elif f(x1) > f(x2):
            a = x2
        else:
            a = x1
            b = x2
    return (a + b) / 2.0

def fibonacci(n):
    return int((((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n) / math.sqrt(5))

def fibonacci_method(a, b, e = 1e-4, i = 0):
    while (a+b) / e  >= fibonacci(i):
        i += 1
    i -= 1
    fib0 = fibonacci(i - 2)
    fib1 = fibonacci(i - 1)
    fib2 = fibonacci(i)
    x1 = a + fib0 / fib2 * (b - a)
    x2  = a + fib1 / fib2 * (b - a)
    while b - a > e:    
        x1 = a + fib0 / fib2 * (b - a)
        x2  = a + fib1 / fib2 * (b - a)
        if f(x1) < f(x2):
            b = x2
        elif f(x1) > f(x2):
            a  = x1
        else:
            a = x1
            b = x2
    return (x1 + x2) / 2