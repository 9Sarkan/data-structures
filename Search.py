def linear(arr, key):
    """
    :type arr: array, np.array
    :type key: int,byte, float, ...
    :return: boolean
    """
    flag = False
    for i in range(len(arr)):
        if arr[i] == key:
            flag = True
            break
    return flag


def Binary(arr, key):
    """
    :type arr: list or numpy.array
    :type key: int, float, double, ...
    :return: boolean
    """
    left = 0
    right = len(arr) - 1
    flag = False
    while left <= right:
        mid = int((left + right) / 2)
        if arr[mid] == key:
            print('Found at %d' % mid)
            flag = True
            break
        else:
            if key > arr[mid]:
                left = mid + 1
            else:
                right = mid - 1
    if not flag:
        print('not Found')
    return flag
