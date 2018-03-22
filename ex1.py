from matplotlib import pyplot as plt
import numpy as np
import math


# function f(x)
def fun(x):
    return np.exp(np.sin(x)**3) + pow(x, 6) - 2*pow(x, 4) - pow(x, 3) - 1


# derivative of f(x)
def der_fun(x):
    return 3*np.exp(np.sin(x)**3)*np.cos(x)*(np.sin(x)**2) + 6*(pow(x, 5)) - 8*(pow(x, 3)) - 3*(pow(x, 2))


'''
# Newton Raphson Method
Receives as arguments:
////////// x0(A random number from the domain of the function)
////////// e (The error)
////////// it (Number of iterations)
'''


def newton(x0, e, it):
    print("Newton Raphson Function:")
    for num_iter in range(it):
        x1 = x0 - fun(x0)/der_fun(x0)
        if(abs(x1-x0)<e):
            print ('Root is at: ', "{0:.6f}".format(x0))
            print ('f(x) at root is: ', fun(x0))
            print ('Number of iterations ', num_iter)
            if der_fun(x0) != 0:
                print("The function's convergence is square, f'(x0) = ", "{0:.6f}".format(der_fun(x0)))
            else:
                print("The function's convergence is not square, f'(x0) = ", "{0:.6f}".format(der_fun(x0)))
            return x1
        else:
            x0 = x1
            print("Checked possible root: ", "{0:.6f}".format(x0))
    return False


'''
# Secant Method 
Receives as arguments:
////////// x0,x1(The edges of the function)
////////// e (The error)
////////// it (Number of iterations)
'''


def secant(x0, x1, e, it):
    print("Secant Function:")
    for num_iter in range(it):
        x2 = x1 - fun(x1)*((x1-x0)/(fun(x1)-fun(x0)))
        if abs (x2 - x1) < e:
            print('Root is at: ', "{0:.6f}".format(x0))
            print('f(x) at root is: ', "{0:.6f}".format(fun(x0)))
            print('Number of iterations ', num_iter)
            if der_fun(x0) != 0:
                print("The function's convergence is square, f'(x0) = ", "{0:.6f}".format(der_fun(x2)))
            else:
                print("The function's convergence is not square, f'(x0) = ", "{0:.6f}".format(der_fun(x2)))
            return x2
        else:
            x0 = x1
            x1 = x2
            print("Checked possible root: ", "{0:.6f}".format(x1))
    print("Solution was not found in ", num_iter ," iterations")
    return False


'''

# function that returns the middle between 2 edges

'''


def mean(begin, end):
    return (begin + end)/2


'''
# Bisection Method
It just receives the two edges of the function
'''


def bisect(edge):
    print("Bisection Function:")
    num_iter = math.ceil((np.log(4) - np.log(0.0000005))/np.log(2))
    for i in range(1,num_iter):
         print(i," Itteration")
         m = mean(edge[0], edge[1])
         print("Mean = ",m)
         if fun(edge[0])*fun(m)<0:
             edge = [edge[0], m]
             print("New Edge ",edge)
         elif fun(edge[1])*fun(m) < 0:
             edge = [m, edge[1]]
             print("New Edge ",edge)
         elif fun(m) == 0:
             print("The root is","{0:.6f}".format(fun(m))," at ","{0:.6f}".format(m),"and was found on ", i , " Itteration")
             if der_fun(m) != 0:
                 print("The function's convergence is square, f'(x0) = ", "{0:.6f}".format(der_fun(m)))
             else:
                 print("The function's convergence is not square, f'(x0) = ", "{0:.6f}".format(der_fun(m)))
             break
    return m


# The two edges of the function
edge = [-2.0, 2.0]
y1 = newton(0.0003, 0.0000005, 100)
print("")
y2=secant(-2.0, 2.0, 0.0000005, 1000)
print("")
y3 = bisect(edge)
x = np.linspace(-2.0, 2.0, 1000)
plt.plot(x, fun(x), 'r', label = 'Function')
plt.plot()
plt.xlabel('Domain')
plt.ylabel("F(x)")
plt.legend
plt.show()
