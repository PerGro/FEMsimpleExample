from .matrix import Matrix
from .abnormalConditions import *
import copy


class Functions:
    @staticmethod
    def same_dimension(matl, matr):
        if isinstance(matl, Matrix) and isinstance(matr, Matrix) is False:
            raise MatrixTypeError()
        cull = len(matl.matrix[0])
        rowr = len(matr.matrix)
        if rowr == cull:
            return True
        else:
            return False

    @staticmethod
    def get_information(matl, matr):
        rowl = len(matl.matrix)
        if isinstance(matl.matrix[0], int):
            pass
        else:
            cull = len(matl.matrix[0])
        rowr = len(matr.matrix)
        if isinstance(matr.matrix[0], int):
            pass
        else:
            culr = len(matr.matrix[0])
        return rowl, cull, rowr, culr

    @staticmethod
    def split_matrix(mat):
        res = []
        for i in range(len(mat.matrix)):
            res.append(mat.matrix[i])
        return res

    @staticmethod
    def split_matrix_thorough(mat):
        res = []
        for i in range(len(mat)):
            for j in range(len(mat.matrix[0])):
                res.append(mat.matrix[i][j])
        return res

    @staticmethod
    def find_cofactor(mat, row, cul):
        matrix_list = copy.deepcopy(Functions.split_matrix(mat))
        temp = matrix_list.pop(row)
        if len(matrix_list):
            for i in range(len(matrix_list)):
                matrix_list[i].pop(cul)
            if len(matrix_list) == 1:
                return matrix_list[0][0]
            return matrix_list
        else:
            return [temp]

    @staticmethod
    def fac(n):
        if n == 0 or n == 1:
            return n
        else:
            return n * Functions.fac(n)

    @staticmethod
    def inverse_number(num_list):
        count = 0
        for i in range(len(num_list)):
            for j in range(i + 1, len(num_list)):
                if num_list[i] > num_list[j]:
                    count += 1
        return count & 1 == 0

    @staticmethod
    def perm(num_list, res_list, current):
        if current == len(num_list) - 1:
            _ = copy.deepcopy(num_list)
            res_list.append(_)
        else:
            for i in range(current, len(num_list)):
                num_list[i], num_list[current] = num_list[current], num_list[i]
                Functions.perm(num_list, res_list, current + 1)
                num_list[i], num_list[current] = num_list[current], num_list[i]

    @staticmethod
    def scan_diagonal(mat_list1, mat_list2):
        for i in range(len(mat_list1)):
            for j in range(len(mat_list1)):
                if mat_list1[i][j] == round(mat_list2[i][j], 0):
                    continue
                else:
                    return False
        return True








