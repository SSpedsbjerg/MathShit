import numpy as math; #Hey, I'm used to C#
from sympy import * ; #I want actuall functions
import time
e = math.exp(1);

#Returns the same function, just looks a lot different as it uses sympy to make the function
#this also makes it easier/more possible to automate it
x = Symbol('x') # You should know what x is when it comes to mathmatical functions, this is just to tell it that x is the counting value

def getCal():
    global x
    equation = -20 * e ** ( - ( (x**2)/8) ) - e ** (0.5 * cos(2*math.pi*x)) + 20 + e
    return equation

def diffEquation(equation):
    global x
    primed = equation.diff(x)
    return primed

def NewtonsMethod(currentX, equation, runs):
    global x
    value = currentX
    i = 0
    diffEquation1 = diffEquation(equation) #differentiate by the first f'(X) 
    diffEquation2 = diffEquation(diffEquation1) #differentiate again f''(X) 
    f1 = lambdify(x, diffEquation1, 'numpy') #make it so it's possible for numpy to use the functions
    f2 = lambdify(x, diffEquation2, 'numpy')
    while runs > i:
        tempValue = value
        deltaX = f1(value)/f2(value)
        value = value - deltaX
        i = i + 1
        #if there is next to no change between the values, just go to the next numbers instead of getting the smallest numbers in difference
        #the speed is the same, whether you use this if statement or not, has been tasted with 100, 0.01, without had 938 sec, with 934 sec.
        '''
        if round(tempValue, 3) == round(value, 3):
            i = runs
            '''
    return round(value, 2)#nobdy wants to see millions of numbers, and don't get me started on scientific, round() defeats both

#TODO: Lav Approx til tallet, derfra tag den til Newtons metode for at komme tættere på
def findCriticalNumbers(min, max, change, equation):
    print("Finding Critpoints")
    CriticalPoints = []
    total = min
    tempAlpha = min
    diffEquation1 = diffEquation(equation)
    while total <= max:
        f = lambdify(x, diffEquation1, 'numpy')
        alpha = f(total)
        #The function has a lucky critical point
        if alpha == 0:
            CriticalPoints.append(total)
        #all the other times
        else:
            value = NewtonsMethod(total, equation, 50)
            #make sure no duplicates gets to the list
            if value not in CriticalPoints:
                CriticalPoints.append(value)
        total = round(total + change, 2);
    return CriticalPoints


if __name__ == '__main__':
    #findCriticalNumbers takes start position on x, and then end, then how often it's going to calculate, then the equation
    #minimum 0.01 for the third input
    timer0 = time.time()
    print("Starting...")
    critPoints = findCriticalNumbers(0, 100, 0.01, getCal())
    print("Sorting results...")
    sorted(critPoints)
    print("DONE!")
    print(critPoints)
    timer1 = time.time() - timer0
    totalTime = str(timer1)
    print("Completed in: " + totalTime + " Sec.")