from pandas import DataFrame
from pymatrix import Operation


def topandas(mat, header=None):
    res = DataFrame()
    mat = Operation.transposition(mat)
    if header is None:
        for i in range(len(mat)):
            res.insert(i, '{}'.format(i), mat.matrix[i])
    else:
        for i in range(len(mat)):
            res.insert(i, header[i], mat.matrix[i])
    return res
