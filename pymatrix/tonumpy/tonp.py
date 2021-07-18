import numpy as np


def tonumpy(mat):
    temp = []
    for i in range(len(mat)):
        temp.append(mat.matrix[i])
    res = np.array(temp)
    return res
