
import numpy as np



'''
Perform an LU decomposition in a given matrix.
#(1) We extract the b vector from the matrix given to the function
(it is the last column of the vector)
#(2) We fill the L matrix and its diagonal with 1
#(3) We fill the U matrix 
#(4) The we find U and L matrices. There may appear some problems like
pivot is zero or pivot is very small in contrast with the other numbers.
That's why before every iteration we find the absolute biggest number in the
array and swap the rows. Then we start pivoting and making every number below
pivot, equal to zero.
#(5) We solve the equation Ly=b and we find a y matrix
#(6) Then we solve the equation Ux = y and we find the solutions matrix x

###
We give an example matrix below
###


'''


def LU(A):
    array_len = len(A)
    b = [0 for i in range(array_len)]
    for i in range(0, array_len):
        b[i] = A[i][array_len]
    L = [[0 for i in range(array_len)] for i in range(array_len)]
    for i in range(0, array_len):
        L[i][i] = 1
    U = [[0 for i in range(0, array_len)] for i in range(array_len)]
    for i in range(0, array_len):
        for j in range(0, array_len):
            U[i][j] = A[i][j]
    array_len = len(U)
    for i in range(0, array_len):
        maxElem = abs(U[i][i])
        maxRow = i
        for k in range(i + 1, array_len):
            if (abs(U[k][i]) > maxElem):
                maxElem = abs(U[k][i])
                maxRow = k
        for k in range(i, array_len):
            tmp = U[maxRow][k]
            U[maxRow][k] = U[i][k]
            U[i][k] = tmp
        for k in range(i + 1, array_len):
            c = -U[k][i] / float(U[i][i])
            L[k][i] = -c
            for j in range(i, array_len):
                U[k][j] += c * U[i][j]
        for k in range(i + 1, array_len):
            U[k][i] = 0
    y = [0 for i in range(array_len)]
    for i in range(array_len):
        y[i] = b[i] / float(L[i][i])
        for k in range(i):
            y[i] -= y[k] * L[i][k]
    ny = np.asarray(y)
    array_len = len(U)
    x = [0 for i in range(array_len)]
    nx = np.asarray(x)
    for i in range(array_len - 1, -1, -1):
        nx[i] = ny[i] / float(U[i][i])
        for k in range(i -1 , -1, -1):
            nx[i] -= nx[k] * U[i][k]
    return nx


'''
Below is implemented a Gaus-Seidel method.
#(1) Define a matrix a of unknown factors
#(2) Define a matrix b of the equalities
#(3) Define a matrix x of n rows filled with zeros at first
#(4) Perfom Gauss-Seidel in a big range eg. 10000
#(5) xabs is the absolute solution and xabsprev is the previous absolute
solution. Perform a substraction between these
'''


def gauss_seidel(n):

    '''
    Test matrices
    #a = [[3,1,-2],[2,-4,-2],[1,1,3]]
    #b = [1/2,1,-2]
    #x = [0.0,0.0,0.0]
    '''

    a=[[0.0] * n for i in range(n)]
    for i in range(n-1):
        a[i][i] = 5
        a[i+1][i] = -2
        a[i][i+1] = -2
    a[n-1][n-1] = 5
    b = [0]*n
    b[0]=3
    b[n-1]=3
    for i in range(1,n-1):
        b[i]=1
    print(b)
    x = [0]*n
    len_a = len(a)
    len_b = len(b)
    for m in range(1,10000):
        xprev = []
        for i in x:
            xprev.append(i)
        for i in range(len_a):
            t = 0
            for j in range(len_a):
                if j != i:
                    t += a[i][j]*x[j]
            t1 = t
            x[i] = (1/a[i][i])*(b[i]-t1)
        xabs = [abs(number)for number in x]
        xprevabs = [abs(number)for number in xprev]
        p = []
        for i in range(3):
            p.append(abs(xabs[i]-xprevabs[i]))
        maxp = max(p)
        if maxp <= 0.0001:
            print("The difference is: "+str(maxp))
            print("Number of iterations: "+str(m))
            break
    z = 0
    for i in x:
        z += 1
        print("Solution number "+str(z) + " {0:.6f}".format(i))


print("The LU decomposition")
print(LU([[1.0,1.0,-1.0,4.0],
               [1.0,-2.0,3.0,-6.0],
               [2.0,3.0,1.0,7.0]]))
print("")
print("Gauss-Seidel")
print(gauss_seidel(10)) #Please give a number n
