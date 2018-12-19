import numpy as np

def swap(arr, E1, E2):
    """
    :type arr: list, numpy.array
    :type E1: int, byte, ...
    :type E2: int, byte, ...
    """
    arr[E1], arr[E2] = arr[E2], arr[E1]


def Selection(arr):
    """
    :type arr: list, numpy.array
    """
    n = len(arr)
    i = 0
    while i < n - 1:
        min = arr[i]
        loc = i
        j = i + 1
        while j < n:
            if arr[j] < min:
                min = arr[j]
                loc = j
            j += 1
        swap(arr, i, loc)
        i += 1


def partition(arr, p, q):
    """
    :type arr: list, numpy.array
    :type p: int, byte, ...
    :type q: int, byte, ...
    """
    x = arr[p]
    i = p
    j = i + 1
    while j <= q:
        if arr[j] <= x:
            i += 1
            swap(arr, i, j)
        j += 1
    swap(arr, i, p)
    return i


def Quick(arr, p, r):
    """
        :type arr: list, numpy.array
        :type p: int, byte, ...
        :type r: int, byte, ...
        """
    if p < r:
        q = partition(arr, p, r)
        Quick(arr, p, q - 1)
        Quick(arr, q + 1, r)


def Bubble(arr):
    """
    :type arr: list, numpy.array
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def Insertion(arr):
    """
    :type arr: list, numpy.array
    """
    n = len(arr)
    for i in range(n):
        j = i
        while arr[j - 1] > arr[j] and j > 0:
            swap(arr, j, j - 1)
            j -= 1


def MaxAndMin(arr):
    """
    :type arr: list, numpy.array
    """
    min = arr[0]
    max = arr[0]
    for i in range(1, len(arr)):
        if max < arr[i]:
            max = arr[i]
        if min > arr[i]:
            min = arr[i]
    return min, max
