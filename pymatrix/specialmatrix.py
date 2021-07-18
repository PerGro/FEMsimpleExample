from pymatrix import Operation
from pymatrix.matrix import Matrix
from pymatrix.abnormalConditions import *
import random
import copy
import math


class Spmatrix(Matrix):
    """
    该类提供各种特殊矩阵的快速创建
    """

    def __init__(self):
        super().__init__()
        self.matrix = Matrix()

    def __add__(self, other):
        super().__add__(other)

    def __mul__(self, other):
        super().__mul__(other)

    '''
    V1.0.0：创建一个稀疏矩阵，目前来说逻辑层上还有较大问题，尽量避免在当前版本使用该方法（尽管使用起来还好）
    '''

    def sparse(self, dimension, sparse_num=0.9):
        if sparse_num < 0.7:
            raise IllegalDataError('greater than 0.7')
        temp = []
        for i in range(dimension ** 2):
            temp.append(0)
        lens = len(temp)
        n = int(lens * (1 - sparse_num))
        if n == 0:
            n += 1
        for i in range(n):
            index = random.randint(0, lens - 1)
            if temp[index] == 0:
                temp[index] = random.randint(0, 9)
        self.square(dimension, num_list=temp)
        return self

    def uper_ting(self, n, model=1, full=None):
        matrix_list = []
        if model == 1:
            temp = []
            for i in range(n):
                temp.append(1)
            for i in range(n):
                copy_l = copy.deepcopy(temp)
                for j in range(i):
                    copy_l.pop(0)
                    copy_l.append(0)
                matrix_list.append(copy_l)
            self.get_matrix(matrix_list)
            return self
        elif model == 2:
            temp = []
            for i in range(n):
                temp.append(1)
            for i in range(n):
                copy_l = copy.deepcopy(temp)
                for j in range(i):
                    copy_l.pop()
                    copy_l.insert(0, 0)
                matrix_list.append(copy_l)
            self.get_matrix(matrix_list)
            return self
        elif model == 3:
            temp = []
            for i in range(n):
                temp.append(0)
            for i in range(n):
                copy_l = copy.deepcopy(temp)
                for j in range(i + 1):
                    copy_l.pop(0)
                    copy_l.insert(n - 1, 1)
                matrix_list.append(copy_l)
            self.get_matrix(matrix_list)
            return self

    def three_digonal(self, n, datalist=None):
        if n < 3:
            raise MatrixSizeError('biger than 3')
        if datalist is None:
            datalist = []
            i = 4 + (n - 2) * 3
            for m in range(i):
                datalist.append(1)
        else:
            if len(datalist) < 4 + (n - 2) * 3:
                i = 4 + (n - 2) * 3 - len(datalist)
                for m in range(i):
                    datalist.append(1)
        index_list = []
        _ = 1
        i = 0
        while i < n ** 2:
            if _ <= 2:
                index_list.append(i)
                _ += 1
                i += 1
            else:
                _ = 0
                i += n - 2
        index_int = 0
        for i in range(n ** 2):
            if i != index_list[index_int]:
                datalist.insert(i, 0)
            else:
                index_int += 1
        self.square(n, datalist[:n ** 2])
        return self

    def diagonal(self, dimension, numfull=1):
        temp = []
        for i in range(dimension):
            temp.append([])
            for j in range(dimension):
                temp[i].append(0)
            temp[i].pop(i)
            temp[i].insert(i, numfull)
        self.get_matrix(temp)
        return self

    def rotation(self, dimension, angle, vector=None):
        if dimension > 3:
            print('the dimension must < 3')
            return 0
        elif dimension == 2:
            temp = [[math.cos(angle), -1 * math.sin(angle)], [math.sin(angle), math.cos(angle)]]
        elif dimension == 3 and vector is not None:
            temp = [[math.cos(angle) + (1 - math.cos(angle)) * vector[0] ** 2, (1 - math.cos(angle)) * vector[0] * vector[1] - math.sin(angle) * vector[2], (1 - math.cos(angle)) * vector[0] * vector[2] + math.sin(angle) * vector[1]],
                    [(1 - math.cos(angle)) * vector[0] * vector[1] - math.sin(angle) * vector[2], math.cos(angle) + (1 - math.cos(angle)) * vector[1] ** 2, (1 - math.cos(angle)) * vector[2] * vector[1] - math.sin(angle) * vector[0]],
                    [(1 - math.cos(angle)) * vector[0] * vector[2] - math.sin(angle) * vector[1], (1 - math.cos(angle)) * vector[2] * vector[1] + math.sin(angle) * vector[2], math.cos(angle) + (1 - math.cos(angle)) * vector[2] ** 2]]
        else:
            print('please input a right dimension')
            return 0
        for i in range(len(temp)):
            for j in range(len(temp)):
                temp[i][j] = round(temp[i][j], 3)
        # self.get_matrix(temp)
        res_matrix = Matrix(temp)
        return res_matrix

    def rotation_enler(self, angle_precession, angle_nutation, angle_spin, res=False, **kwargs):
        z_vector = kwargs.get('z_vector', [0, 0, 1])
        x_vector = kwargs.get('x_vector', [1, 0, 0])
        rounder = kwargs.get('rounder', 3)
        matrix_precession = self.rotation(3, angle_precession, z_vector)
        matrix_nutation = self.rotation(3, angle_nutation, x_vector)
        m_z_vector = Matrix([z_vector])
        z_vector = list(Operation().mul(m_z_vector, matrix_nutation).matrix[0])
        matrix_spin = self.rotation(3, angle_spin, z_vector)
        matrix_list = [matrix_precession, matrix_nutation, matrix_spin]
        if res:
            res_matrix = Operation().mul(Operation.mul(matrix_list[0], matrix_list[1]), matrix_list[2])
            for i in range(len(res_matrix.matrix)):
                for j in range(len(res_matrix.matrix[0])):
                    res_matrix.matrix[i][j] = round(res_matrix.matrix[i][j], rounder)
            return res_matrix
        for matrix in matrix_list:
            num = 0
            for i in range(len(matrix.matrix)):
                for j in range(len(matrix.matrix[i][0])):
                    matrix_list[num].matrix[i][j] = round(matrix_list[num].matrix[i][j], rounder)
            num += 1
        return matrix_list




