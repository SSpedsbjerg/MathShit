import numpy as math;
from sympy import * ;

e = math.exp(1);

#Returns the same function, just looks a lot different
x = Symbol('x')
def getCal():
    global x;
    equation = -20 * e ** ( - ( (x**2)/8) ) - e ** (0.5 * cos(2*math.pi*x)) + 20 + e;
    return equation;

def diffEquation(equation):
    global x;
    primed = equation.diff(x);
    return primed;


#TODO: Lav Approx til tallet, derfra tag den til Newtons metode for at komme tættere på
def findCriticalNumbers(min, max, change, equation):
    total = min
    tempAlpha = min
    while total != max:
        tempAlpha = diffEquation(equation)
        total = total + change;


if __name__ == '__main__':
    function0 = getCal();
    function1 = diffEquation(function0);
    function2 = diffEquation(function1);
    print(function0);
    print(function1);
    print(function2);