def Muze(grid, x, y):
    """
    :type grid: numpy.matrix
    :type x: int
    :type y: int
    :return: boolean
    """
    if grid[x][y] == 2:
        print('Found at x : {0} - y : {1}'.format(x, y))
        return True
    elif grid[x][y] == 1:
        print('Visit Wall at x : {0} - y : {1}'.format(x, y))
        return False
    elif grid[x][y] == 3:
        print('visited at x : {0} - y : {1}'.format(x, y))
        return False
    print('visiting x : {0} - y : {1}'.format(x, y))
    # set as visited
    grid[x][y] = 3

    if ((y < len(grid) - 1 and Muze(grid, x, y + 1)) or
        (x < len(grid) - 1 and Muze(grid, x + 1, y)) or
        (0 < y and Muze(grid, x, y - 1)) or
        (0 < x and Muze(grid, x - 1, y))):
        return True

    return False


# test
grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]

Muze(grid, 0, 0)
