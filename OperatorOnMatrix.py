import numpy as np
import random as rand

def full(a, b, r=100, datatype=int):
    """
    :type a: int, ...
    :type b: int, ...
    :type r: int, ...
    :type datatype: <class 'type'>
    """
    matrix = np.zeros((a, b), dtype=datatype)
    i = 0
    while i < a:
        j = 0
        while j < b:
            matrix[i][j] = rand.randrange(r)
            j += 1
        i += 1
    return matrix


def sumMatrix(Ma, Mb, datatype=int):
    """
    :type Ma: numpy.matrix
    :type Mb: numpy.matrix
    :type datatype: <class 'type'>
    :return: numpy.matrix
    """
    if Ma.shape != Mb.shape:
        print('The Matrix shape is not equal.')
        return -1
    lst = Ma.shape
    i, j = lst[0], lst[1]
    zero = np.zeros((i, j), dtype=datatype)
    z = 0
    while z < i:
        x = 0
        while x < j:
            zero[z][x] = Ma[z][x] + Mb[z][x]
            x += 1
        z += 1
    return zero


def minusMatrix(Ma, Mb, datatype=int):
    """
    :type Ma: numpy.matrix
    :type Mb: numpy.matrix
    :type datatype: <class 'type'>
    :return: numpy.matrix
    """
    if Ma.shape != Mb.shape:
        print('The Matrix shape is not equal.')
        return -1
    lst = Ma.shape
    i, j = lst[0], lst[1]
    zero = np.zeros((i, j), dtype=datatype)
    z = 0
    while z < i:
        x = 0
        while x < j:
            zero[z][x] = Ma[z][x] - Mb[z][x]
            x += 1
        z += 1
    return zero


def multiMatrix(Ma, Mb, datatype=int):
    """
    :type Ma: numpy.matrix
    :type Mb: numpy.matrix
    :type datatype: <class 'type'>
    :return: numpy.matrix
    """
    lst = Mb.shape
    m = lst[1]
    lst_ = Ma.shape
    i, j = lst_[0], lst_[1]
    if lst[0] != lst_[1]:
        print('the condition is not true.')
        return -1
    zero = np.zeros((i, m), dtype=datatype)
    z = 0
    while z < i:
        x = 0
        while x < m:
            zero[z][x] = 0
            k = 0
            while k < j:
                zero[z][x] += Ma[z][k] * Mb[k][x]
                k += 1
            x += 1
        z += 1
    return zero


def getMatrixShape(matrix):
    """
    :type matrix: numpy.matrix
    :return: <class 'list'>
    """
    i = 0
    j = 0
    while True:
        try:
            a = matrix[0][i]
            i += 1
        except:
            break
    while True:
        try:
            b = matrix[j][0]
            j += 1
        except:
            break
    return [j, i]


def getUnEmpty(matrix):
    """
    :type matrix: numpy.matrix
    :return: <class 'list'>
    """
    lst = getMatrixShape(matrix)
    # lst = matrix.shape
    i, j = lst[0], lst[1]
    m = 0
    lst = []
    while m < i:
        n = 0
        while n < j:
            if matrix[m][n] != 0:
                lst.append([m, n, matrix[m][n]])
            n += 1
        m += 1
    return lst


def makeN3Table(matrix):
    """
    :type matrix: numpy.matrix
    :return: numpy.matrix
    """
    ue = getUnEmpty(matrix)
    lst = getMatrixShape(ue)
    matInfo = getMatrixShape(matrix)
    n3 = np.zeros((lst[0] + 1, 3), dtype=int)
    n3[0][0] = matInfo[0]
    n3[0][1] = matInfo[1]
    n3[0][2] = lst[0]
    i = 1
    while i < lst[1]:
        j = 0
        while j < 3:
            n3[i][j] = ue[i - 1][j]
            j += 1
        i += 1
    return n3


# test ============================================================
i = 2
j = 3
m = 4
A = full(i, j, 10)
B = full(i, j, 20)
C = full(j, m, 10)
print('A : \n', A, '\nB : \n', B, '\nC : \n', C)
print('========================================')
D = sumMatrix(A, B)
print(D)
print('========================================')
E = minusMatrix(A, B)
print(E)
print('========================================')
F = multiMatrix(A, C)
print(F)
# text n3
print('========================================')
mat = np.zeros((3, 4)).astype(int)
mat = [[0, 2, 0, 0],
       [1, 0, 1, 0],
       [0, 0, 3, 0]]
print(mat)
print('==========================')
print(getMatrixShape(mat))
print('==========================')
print(getUnEmpty(mat))
print('==========================')
print(makeN3Table(mat))
