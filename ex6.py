from matplotlib import pyplot as plt
import numpy as np
import math



'''
The second derivative of F function
'''

def ddf(x):
    return -math.sin(x)


'''
The third derivative of F function
'''


def ddddf(x):
    return math.sin(x)


'''
The trapezodial function that returns the area of the function sin
'''


def Trapezodial(n):
    y=0
    for i in range(1,n-2):
        y = y + 2 * y_arr[i]
    y1 = ((end-begin)/(2*n))*(y + y_arr[0] + y_arr[n - 1])
    return y1


'''
The Simpson function that returns the area of the function sin
'''


def Simpson(n):
    y = 0
    for i in range(1,int((n/2)-1)):
        y = y + 2 * y_arr[2 * i]
    y1 = 0
    for i in range(1,int((n/2))):
        y1 = y1 + 4 * y_arr[2 * i - 1]
    x = ((end-begin)/(3*n))*(y_arr[0] + y_arr[n - 1] + y + y1)
    return x


begin = 0
end = math.pi/2
edge=[begin,end]
y_arr=[]
x_arr = np.random.uniform(begin,end,10)


for i in x_arr:
    y_arr.append(math.sin(i))

max2 = abs(ddddf(end))
e2 = ((pow(end-begin,5)) / (180 * (len(y_arr) ** 4))) * max2
print(e2)
max = abs(ddf(end))
e = ((end-begin)**3) / (12 * len(y_arr)) * max
print(e)


trap = Trapezodial(len(y_arr))
print(trap)
simp = Simpson(len(y_arr))
print(simp)
X = np.linspace(begin, end, 10)
plt.plot(X, y_arr)
plt.show()
