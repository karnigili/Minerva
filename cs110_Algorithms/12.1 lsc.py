import numpy as np
from pandas import *
import random 

def LCS_len (x,y):
    m = len(x)
    n = len(y)
    
    # b = [[None] * (len(y)+1) for _ in range(len(x)+1)]

    LSC = [[0] * (len(y)+1) for _ in range(len(x)+1)]


    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):

            if x[i-1] == y[j-1] :
                LSC[i][j] = LSC[i-1][j-1]+ 1
                # b[i][j] = 'upleft'
            

            elif LSC[i-1][j] >= LSC[i][j-1]:
                LSC[i][j] = LSC[i-1][j]
                # b[i][j] = 'up'

            else:
                LSC[i][j] = LSC[i][j-1]
                # b[i][j] ='left'

    return LSC#, b


def backtrack (lcs, x, y, i = None, j = None):
    if i == None : 
        i = len(x)

    if j == None:
        j = len(y)


    if i == 0 or j == 0:
        return ""

    
    elif x[i-1] == y[j-1]:
        return backtrack(lcs, x, y, i-1, j-1) + str(x[i-1])
    
    else:
        if lcs[i][j-1] > lcs[i-1][j]:
            return backtrack(lcs, x, y, i, j-1)
        else:
            return backtrack(lcs, x, y, i-1, j)


def all_backtrack (lcs, x, y, i = None, j = None):
    if i == None : 
        i = len(x)

    if j == None:
        j = len(y)

    if i == 0 or j == 0:
        return set([""])

    if x[i-1] == y[j-1]:
        return set([string + str(x[i-1]) for string in all_backtrack(lcs, x, y, i-1, j-1)])

    else:
        set_of_lcs = set()

        if lcs[i][j-1] >= lcs[i-1][j]:
            set_of_lcs.update (all_backtrack(lcs, x, y, i, j-1))
        if lcs[i-1][j] >= lcs[i][j-1]:
            set_of_lcs.update (all_backtrack(lcs, x, y, i-1, j))


        return set_of_lcs








A = ['A', 'B', 'C', 'B', 'D', 'A', 'B'] 
B = ['B', 'D', 'C', 'A', 'B', 'A']
h = [1, 0, 0, 1, 0, 1, 0, 1] 
j = [0, 1, 0, 1, 1, 0, 1, 1, 0]

l = [random.randint(0,9) for _ in range(5)]

str1 = A
str2 = B

# print str1, str2

# print_LCS(b, A, len(A),len(B))
# print backtrack(c, A, B)

print all_backtrack(LCS_len(str1, str2), str1, str2)
# print DataFrame(b)
# print DataFrame(c)


