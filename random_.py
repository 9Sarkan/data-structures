import random as rand
import numpy as np

# make a number in range(0,10)
a = rand.randrange(10)
# make a number in range(5,10)
b = rand.randint(5, 10)
# make a number in range(5,10,2)
c = rand.randrange(5, 10, 2)

arr = np.zeros(10).astype(int)
for i in range(0, 10):
    arr[i] = rand.randrange(100)
