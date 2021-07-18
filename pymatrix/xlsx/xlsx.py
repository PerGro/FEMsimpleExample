from pandas import read_csv
import pandas.core
from pymatrix import Matrix
from pymatrix import Operation
import time

__now_time__ = time.strftime('%Y%m%d%H%M%S ', time.localtime(time.time()))


def open_csv(path, header=None):
    matrix = Matrix()
    if header is None:
        pds = read_csv(path, header=None)
    else:
        pds = read_csv(path, header=header)
    temp = []
    for i in range(len(pds)):
        temp.append(pds.loc[i])
    matrix.get_matrix(temp)
    return matrix


def wirte_csv(mat, path, name=None, header=None):
    pad = pandas.DataFrame()
    mat = Operation.transposition(mat)
    if header is None:
        for i in range(len(mat)):
            pad.insert(i, '{}'.format(i), mat.matrix[i])
    else:
        for i in range(len(mat)):
            pad.insert(i, '{}'.format(header[i]), mat.matrix[i])
    if name is not None:
        pad.to_csv(r'{}'.format(path) + '\\' + name + '.csv')
    else:
        pad.to_csv(r'{}'.format(path) + '\\' + str(__now_time__) + '.csv')
