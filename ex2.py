from matplotlib import pyplot as plt
import numpy as np
import math
import random


'''
Function f(x)
'''


def fun(x):
    return 54*pow(x,6) + 45*pow(x,5) -102*pow(x,4) - 69*pow(x,3) + 35*pow(x,2) + 16*x - 4


'''
Derivative of f(x)
'''


def der_fun(x):
    return 324*pow(x, 5) + 225*pow(x, 4) - 408*pow(x, 3) - 207*pow(x, 2) + 70*x + 16


'''
Second Derivative of f(x)
'''


def dder_fun(x):
    return 1620*pow(x,4) + 900*pow(x,3) - 1224*pow(x,2) - 414*x + 70


'''
A function that returns a random number in the domain of the function
used in bisect
'''


def randNum(begin, end):
    run_m = random.uniform(begin, end)
    return run_m


'''
# Bisection Method
The possible root is not the mean of the edges but a random number inside f domain
'''


def bisectEdit(begin, end):
    print("Bisection Function:")
    N = math.ceil((np.log(4)- np.log(0.0000005))/np.log(2))
    edge = [begin , end]
    for i in range(N):
         run_m = randNum(edge[0], edge[1])
         if fun(edge[0])*fun(run_m)<0:
             edge = [edge[0], run_m]
         elif fun(edge[1])*fun(run_m)<0:
             edge = [run_m, edge[1]]
         elif fun(run_m) == 0:
             print("The root is", "{0:.6f}".format(fun(run_m)), " at ", "{0:.6f}".format(run_m), "and was found on ", i ," Iteration")
             break
    print("The number of iterations to reach the error was exhausted. The iterations were: ",i)
    return run_m


'''
# Newton Raphson Edited Method
Receives as arguments:
////////// x0(A random number from the domain of the function)
////////// e (The error)
////////// it (Number of iterations)
'''


def newtonEdit(x0, e, it):
    print("Newton Raphson Function:")
    for num_iter in range(it):
        x1 = x0 - fun(x0)/der_fun(x0) - 0.5*((fun(x0)**2)*dder_fun(x0))/(der_fun(x0)**3)
        if abs(x1-x0)<e:
            print('Root is at: ', x1)
            print('f(x) at root is: ', fun(x1))
            print('Number of iterations ', num_iter)
            #print(abs(x1-x0))
            return x1
        else:
            x0 = x1
            print("Checked possible root: ", "{0:.6f}".format(x0))
    return False


'''
# Secant Method Edited
Receives as arguments:
////////// x0,x1,x2(The three points)
////////// e (The error)
////////// it (Number of iterations)
'''


def secantEdit(x0, x1, x2, e, it):
    print("Secant Function:")
    q = fun(x0)/fun(x1)
    r = fun(x2)/fun(x1)
    s = fun(x2)/fun(x0)
    for num_iter in range(it):
        x3 = x2 - (r*(r-q)*(x2-x1)+(1-r)*s*(x2-x0))/((q-1)*(r-1)*(s-1))
        if abs(x3-x0)<e:
            print ('Root is at: ', x3)
            print ('f(x) at root is: ', fun(x3))
            print ('Number of iterations ', num_iter)
            return x0
        else:
            x0 = x3
            print("Checked possible root: ", "{0:.6f}".format(x3))
    print("Solution was not found in ", num_iter, " iterations")
    return False


y1 = bisectEdit(-2.0,2.0)
#print("The root was found at: " , "{0:.6f}".format(y1))
print("")
y2 = secantEdit(-2, 0, 2, 0.0000005, 1000)
print("")
y3 = newtonEdit(2, 0.0000005, 100)
x = np.linspace(-2.0, 2.0, 1000)
plt.plot(x, fun(x), 'r', label = 'Function')
plt.plot()
plt.xlabel('Domain')
plt.ylabel("F(x)")
plt.legend
plt.show()