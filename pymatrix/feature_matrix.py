import numpy as np
from pymatrix import Matrix
from pymatrix import Spmatrix
from pymatrix import Operation
import random


class FeatureMatrix(Matrix):
    @staticmethod
    def create_rotation_matrix(dimension, p, q, theta, rou=3):
        matrix_origin = Spmatrix.diagonal(Spmatrix(), dimension, 1)
        matrix_origin.matrix[p][p] = round(np.cos(theta), rou)
        matrix_origin.matrix[p][q] = round(-np.sin(theta), rou)
        matrix_origin.matrix[q][p] = round(np.sin(theta), rou)
        matrix_origin.matrix[q][q] = round(np.cos(theta), rou)

        return matrix_origin


if __name__ == '__main__':
    l = []
    for i in range(5):
        l.append([])
        for j in range(5):
            l[i].append(random.randint(1, 10))
    m = Matrix(l)
    f = FeatureMatrix.create_rotation_matrix(5, 2, 1, 1.047)
    print(m)
    print(f)
    print(Operation.mul(m, f))