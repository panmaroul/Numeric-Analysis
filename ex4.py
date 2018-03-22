import numpy as np
import random as rn
import math as m
# Filling array (A)
def a_matrix():
    A = [[0.0] * 15 for i in range(15)]
    A[0][1]=1.0
    A[0][8]=1.0
    A[1][2]=1.0
    A[1][4]=1.0
    A[1][6]=1.0
    A[2][1]=1.0
    A[2][5]=1.0
    A[2][7]=1.0
    A[3][2]=1.0
    A[3][11]=1.0
    A[4][0]=1.0
    A[4][9]=1.0
    A[5][9]=1.0
    A[5][10]=1.0
    A[6][9]=1.0
    A[6][10]=1.0
    A[7][3]=1.0
    A[7][10]=1.0
    A[8][4]=1.0
    A[8][5]=1.0
    A[8][9]=1.0
    A[9][12]=1.0
    A[10][14]=1.0
    A[11][6]=1.0
    A[11][7]=1.0
    A[11][10]=1.0
    A[12][8]=1.0
    A[12][13]=1.0
    A[13][9]=1.0
    A[13][10]=1.0
    A[13][12]=1.0
    A[13][14]=1.0
    A[14][11]=1.0
    A[14][13]=1.0
    return A


'''
Adding 4 new connections and removing 1 to increase the rank of 5th page.
Please change a_matrix with new_A to the functions to see the results
'''


def new_A(a_matrix):
    A = a_matrix
    A_new = [[0.0] * 15 for i in range(15)]
    for i in range(15):
        for j in range(15):
            A_new[i][j] = A[i][j]
    A_new[9][4] = 1.0
    A_new[10][9] = 1.0
    A_new[5][4] = 1.0
    A_new[13][4] = 1.0
    A_new[0][4] = 0.0
    return A_new


'''
Function for computing the Google matrix
'''


def compute_G(a_mat):
    q = 0.6
    n = []
    for j in range(15):
        sum_of_a = 0.0
        for i in range(15):
            sum_of_a += a_mat[j][i]
        n.append(sum_of_a)
    p = [[0]*15 for i in range(15)]

    # filling p array with the relevant elements
    for i in range(15):
        for j in range(15):
            p[i][j] = (q/15) + ((1-q) * a_mat[j][i]) / n[j]
    pd = [0]*15

    for j in range(15):
        sum5 = 0
        for i in range(15):
            a = (1-q) * (p[i][j]) * a_mat[i][j] / n[i]
            sum5 += ((q*p[i][j])/15) + a
        pd[j] = sum5
    print(pd[4])
    G = [[0.0]*15 for i in range(15)]
    for i in range(15):
        for j in range(15):
            G[i][j] = q / 15 + (a_mat[j][i] * (1 - q)) / n[j]
    return G


'''
The power method function. It receives a random number to use
for choosing a random column in 
'''


def power_method(rand_num):
    b = []
    k = 0
    # The eigenvalue
    l = 0
    G = compute_G(a_matrix()) # !!!!!!!!!!!!!!!!!!!!!!!CHANGE a_matrix TO new_A TO SEE DIFFERENCES!!!!!!!!!!!!!!!!!!!!!!!!!
    for i in range(15):
        b.append(G[i][rand_num])
    while k < 5000:
        # dot is a function of numpy class, used for multiplying matrices
        mult_b = np.dot(b, G)
        # searching for the first non zero (fnz) in mb matrix
        for i in range(15):
            if mult_b[i] != 0:
                fnz = mult_b[i]
                break
        # fills b matrix with every element of mb matrix divided by fnz
        for i in range(15):
            mult_b[i] = mult_b[i] / fnz
            b[i] = mult_b[i]

        if k == 0:
            k += 1
            l = fnz
            continue
        elif abs(l-fnz) < 0.1:
            # Normalization to 1
            nb = np.asarray(b)
            sum_of_b = np.ndarray.sum(nb)
            for i in range(15):
                nb[i] = nb[i] / sum_of_b
            print("The eigenvector is: "+str(nb))
            print("The eigenvalue is: " + str(l))
            return nb

        l = fnz
        k += 1
    return False


rand_num = rn.randint(0,14)
page_rank = power_method(rand_num)
#print(page_rank[4])


'''
A function that checks whether a matrix is stochastic or not
It returns a relevant message
'''


def is_stochastic():
    G = compute_G(a_matrix())
    for j in range(15):
        sum9 = 0
        for i in range(15):
            sum9 += G[i][j]
        if int(sum9) != 1:
            print("The matrix is not stochastic")
            return False
    print("The matrix is stochastic")
    return True


is_stochastic()
