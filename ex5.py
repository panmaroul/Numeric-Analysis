from matplotlib import pyplot as plt
import numpy as np
import math

'''
The deltaArray function returns a deltaarray matrix which contains all the Δ that is used for 
computing the polynomial approximation
'''
def deltaArray():

    deltaarray = np.zeros((len(arraysOfy),len(arraysOfy)))
    for i in range(0, len(arraysOfy)-1):
        deltaarray[i][0]=(arraysOfy[i+1]-arraysOfy[i])/(arraysOfx[i+1]-arraysOfx[i])

    for i in range(1,len(arraysOfy)-1):
        for j in range(0, len(arraysOfy)-i-1):
            deltaarray[i][j]=(deltaarray[i-1][j+1]-deltaarray[i-1][j])/(arraysOfx[i+j+1]-arraysOfx[j])
    return deltaarray


'''
The polynomial functions returns the approximate sum of sin function
'''


def polynomial(x):
    sum1 = arraysOfy[0]
    deltaarray = deltaArray()
    for i in range (0,len(arraysOfy)-2):
        a = float(deltaarray[i][0])
        p = 1
        for j in range(0,i+1):
            p = p*(x-arraysOfx[j])
        sum1 = sum1 + a*p
    return sum1


begin = -3.14
end = 3.14
arraysOfy=[]
arraysOfx = np.random.uniform(begin,end,200 )
sort_arrayx = arraysOfx.sort()
for i in arraysOfx:
    arraysOfy.append(math.sin(i))
print(polynomial(5))
X = np.linspace(begin, end, 200)
plt.plot(X,polynomial(arraysOfy))
plt.show()
