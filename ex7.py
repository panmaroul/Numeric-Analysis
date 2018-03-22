import numpy as np
import random as rn
from matplotlib import pyplot as plt


'''
Gauss function.
#(1) We search the maximum in each column
#(2) We swap the maximum row (column by column) with the current row
#(3) We make all rows below the maximum column equal to zero
#(4) We solve Ax=b (Where A is an upper triangular matrix) 
'''


def gauss(A):
    n = len(A)

    for i in range(0, n):
        maxEl = abs(A[i][i])
        maxRow = i
        for k in range(i+1, n):
            if abs(A[k][i]) > maxEl:
                maxEl = abs(A[k][i])
                maxRow = k

        for k in range(i, n+1):
            tmp = A[maxRow][k]
            A[maxRow][k] = A[i][k]
            A[i][k] = tmp

        for k in range(i+1, n):
            c = -A[k][i]/A[i][i]
            for j in range(i, n+1):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] += c * A[i][j]

    x = [0 for i in range(n)]
    for i in range(n-1, -1, -1):
        x[i] = A[i][n]/A[i][i]
        for k in range(i-1, -1, -1):
            A[k][n] -= A[k][i] * x[i]
    print(A)
    return x


'''
Function that returns the predictable y for a specific day
'''


def f(x, sol):
    sum_f = 0
    for i in range(len(sol)):
        sum_f += pow(x, i) * sol[len(sol) - 1 - i]
    return sum_f



'''
Function that returns the stock we want to predict its closing
I chose 2 stocks. One is ΑΛΜΥ and the other is ΕΛΤΚ
'''


def stock(choise):
    if choise == 0:
        closed_stock = [0.4300, 0.4260, 0.440, 0.4450, 0.4460, 0.4570, 0.4640, 0.4460, 0.4590, 0.4690]
        nclosed_stock = np.asarray(closed_stock)
        ntclosed_stock = np.transpose(nclosed_stock)
        return ntclosed_stock
    elif choise == 1:
        closed_stock = [2.0000, 2.1000, 2.1000, 2.1000, 2.1300, 2.1300, 2.1400, 2.1600, 2.1400, 2.1300]
        nclosed_stock = np.asarray(closed_stock)
        ntclosed_stock = np.transpose(nclosed_stock)
        return ntclosed_stock


'''
Please choose between 0 for ΑΛΜΥ and 1 for ΕΛΤΚ as variables 
'''
stock_to_predict = stock(1)




'''
#################
#This is 3rd degree polynomial. Please comment out to check
#################

A = [[0.0] * 4 for i in range(len(stock_to_predict))]

for i in range(1,len(stock_to_predict)):
    A[i-1][0] = pow(i,3)
    A[i-1][1] = pow(i,2)
    A[i-1][2] = i
    A[i-1][3] = 1
nA=np.asarray(A)
'''


'''
#################
#This is 4th degree polynomial. Please comment out to check
#################

A = [[0.0] * 5 for i in range(len(stock_to_predict))]

for i in range(1,len(stock_to_predict)):
    A[i-1][0] = pow(i,4)
    A[i-1][1] = pow(i,3)
    A[i-1][2] = pow(i,2)
    A[i-1][3] = i
    A[i-1][4] = 1
nA=np.asarray(A)
'''



'''
This is a 2nd degree polynomial
'''
A = [[0.0] * 3 for i in range(len(stock_to_predict))]

for i in range(1,len(stock_to_predict)):
    A[i-1][0] = pow(i,2)
    A[i-1][1] = i
    A[i-1][2] = 1
nA = np.asarray(A)


At = [[0.0] * 10 for i in range(3)]  # Change range(3) to range(4) or range(5) for bigger degree polynomial
nAt = np.asarray(At)
ntAt = np.transpose(nA)
C = np.dot(ntAt,nA)
Z = np.dot(ntAt, stock_to_predict)
C1 = [[0.0] * 4 for i in range(3)]  # Change range(3) to range(4) or range(5) for bigger degree polynomial
nC1 = np.asarray(C1)
for i in range (3):  # Change range(3) to range(4) or range(5) for bigger degree polynomial
    for j in range(3):  # Change range(3) to range(4) or range(5) for bigger degree polynomial
        nC1[i][j] = C[i][j]
for j in range(3):  # Change range(3) to range(4) or range(5) for bigger degree polynomial
    nC1[j][3] = Z[j]


print(nC1)
solutions = gauss(nC1)
print(solutions)
y = f(14,solutions)
print(y)

lin_sp = np.linspace(1,14,10)  # increase the second parameter to 11,12,13,14 to see the predictions
plt.plot(lin_sp, f(lin_sp,solutions))
plt.show()
