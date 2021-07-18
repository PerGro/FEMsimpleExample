from .matrix import Matrix
from .abnormalConditions import *
from .assistfuction import Functions
import numpy as np
import sys

sys.setrecursionlimit(1000000000)


class Operation(Functions):
    def __init__(self):
        pass

    @staticmethod
    def mul(matl, matr):
        if isinstance(matl, Matrix) and isinstance(matr, Matrix) is False:
            raise SubTypeError('matrix')
        if Functions.same_dimension(matl, matr) is False:
            raise MatrixSizeError()
        matrix = Matrix()
        matrix.matrix = []
        rowl, cull, rowr, culr = Functions.get_information(matl, matr)
        for i in range(rowl):
            matrix.matrix.append([])
        for j in range(rowl):
            for i in range(culr):
                temp = []
                for n in range(cull):
                    temp.append(matl.matrix[j][n] * matr.matrix[n][i])
                matrix.matrix[j].append(sum(temp))
        return matrix

    @staticmethod
    def transposition(mat):
        if mat.matrix is None:
            raise SubTypeError('matrix')
        res = []
        for i in range(len(mat.matrix[0])):
            res.append([])
        for i in range(len(mat.matrix[0])):
            for n in range(len(mat.matrix)):
                res[i].append(mat.matrix[n][i])
        matrix = Matrix()
        matrix.matrix = res
        return matrix

    @staticmethod
    def determinant(mat):
        if len(mat.matrix) != len(mat.matrix[0]):
            raise MatrixSizeError()
        res = 0
        res_list = []
        num_list = list(range(len(mat.matrix)))
        Functions.perm(num_list, res_list, 0)
        for i in range(len(res_list)):
            temp_list = res_list[i]
            mi = 1 if Functions.inverse_number(temp_list) else -1
            temp = mi
            row = 0
            for j in range(len(temp_list)):
                col = temp_list[j]
                temp *= mat.matrix[row][col]
                row += 1
            res += temp
        return res

    @staticmethod
    def cut(mat, cut_row, cut_col):
        temp = mat.copy
        if isinstance(cut_row, list):
            begin_r = cut_row[0]
            end_r = cut_row[1]
        else:
            begin_r = cut_row
            end_r = len(temp)
        if isinstance(cut_col, list):
            begin_c = cut_col[0]
            end_c = cut_col[1]
        else:
            begin_c = cut_col
            end_c = len(temp.matrix[0])
        temp.matrix = temp.matrix[begin_r:end_r]
        for i in range(len(temp)):
            temp.matrix[i][:] = temp.matrix[i][begin_c:end_c]
        return temp

    @staticmethod
    def adjoint(mat):
        if len(mat.matrix) != len(mat.matrix[0]):
            raise MatrixSizeError('should be same size')
        res = Matrix()
        res_list = []
        for i in range(len(mat)):
            for j in range(len(mat)):
                mi = 1 if (i + j) % 2 == 0 else -1
                res_list.append((mi * Operation.determinant(Matrix(Functions.find_cofactor(mat, i, j)))))
        res.square(len(mat), res_list)
        return res

    @staticmethod
    def inverse(mat, acc=8):
        det = Operation.determinant(mat)
        if det == 0:
            print('this matrix do not have its inverse matrix')
            return
        temp = Operation.transposition(Operation.adjoint(mat))
        det_matrix = Matrix()
        det_matrix.full(len(mat), len(mat), 1 / det)
        return Matrix.square(Matrix(), len(mat), Functions.split_matrix_thorough(temp * det_matrix))

    @staticmethod
    def isrank(mat1, mat2):
        pass

    @staticmethod
    def rotation(ang):
        pass

    @staticmethod
    def __diagonal(dimension, fillnum):
        temp = []
        for i in range(dimension):
            temp.append([])
            for j in range(dimension):
                temp[i].append(0)
            temp[i].pop(i)
            temp[i].insert(i, fillnum)
        m = Matrix(temp)
        return m

    def feature_matrix(self, matrix, dimension, rou=3, theta=None, eigenvector=None, e=0.01):  # 不考虑无需寻找的情况
        max_num = 0
        p = 0
        q = 0
        for i in range(dimension):
            for j in range(dimension):
                if j > i and abs(matrix.matrix[i][j]) > max_num:
                    max_num = abs(matrix.matrix[i][j])
                    p = i
                    q = j
        # print(p, q)
        if matrix.matrix[q][q] - matrix.matrix[p][p]:
            theta = (np.arctan(-2 * matrix.matrix[p][q]) / (matrix.matrix[q][q] - matrix.matrix[p][p])) / 2
        else:
            theta = np.arcsin(1)
        # print(theta)
        if eigenvector is None:
            eigenvector = self.__diagonal(dimension, 1)
        # diag_matrix = self.__diagonal(dimension, 1)
        # diag_matrix.matrix[p][p] = round(np.cos(theta), rou)
        # diag_matrix.matrix[p][q] = round(-np.sin(theta), rou)
        # diag_matrix.matrix[q][p] = round(np.sin(theta), rou)
        # diag_matrix.matrix[q][q] = round(np.cos(theta), rou)
        temp_a_matrix_pp = matrix.matrix[p][p] * np.cos(theta) ** 2 + matrix.matrix[q][q] * np.sin(theta) ** 2 + 2 * matrix.matrix[p][q] * np.cos(theta) * np.sin(theta)
        temp_a_matrix_qq = matrix.matrix[p][p] * np.sin(theta) ** 2 + matrix.matrix[q][q] * np.cos(theta) ** 2 - 2 * matrix.matrix[p][q] * np.cos(theta) * np.sin(theta)
        temp_a_matrix_pq = 0.5 * (matrix.matrix[q][q] - matrix.matrix[p][p]) * np.sin(2 * theta) + matrix.matrix[p][q] * np.cos(2 * theta)
        temp_a_matrix_qp = temp_a_matrix_pq
        matrix.matrix[p][p] = temp_a_matrix_pp
        matrix.matrix[q][q] = temp_a_matrix_qq
        matrix.matrix[p][q] = temp_a_matrix_pq
        matrix.matrix[q][p] = temp_a_matrix_qp
        for i in range(dimension):
            if i != p and i != q:
                temp_num = matrix.matrix[i][p]
                matrix.matrix[i][p] = matrix.matrix[i][q] * np.sin(theta) + temp_num * np.cos(theta)
                matrix.matrix[i][q] = matrix.matrix[i][q] * np.cos(theta) - temp_num * np.sin(theta)
        for j in range(dimension):
            if j != p and j != q:
                temp_num = matrix.matrix[p][j]
                matrix.matrix[p][j] = matrix.matrix[q][j] * np.sin(theta) + temp_num * np.cos(theta)
                matrix.matrix[q][j] = matrix.matrix[q][j] * np.cos(theta) - temp_num * np.sin(theta)
        for i in range(dimension):
            temp = eigenvector.matrix[i][p]
            eigenvector.matrix[i][p] = eigenvector.matrix[i][q] * np.sin(theta) + temp * np.cos(theta)
            eigenvector.matrix[i][q] = eigenvector.matrix[i][q] * np.cos(theta) - temp * np.sin(theta)
        # 开始迭代
        if max_num <= e:
            eigenvalues = []  # 特征向量
            for i in range(dimension):
                eigenvalues.append(matrix.matrix[i][i])
            for i in range(dimension):
                for j in range(dimension):
                    eigenvector.matrix[i][j] = round(eigenvector.matrix[i][j], rou)
            for i in range(len(eigenvalues)):
                eigenvalues[i] = round(eigenvalues[i], rou)
            eigenvalues = Matrix([eigenvalues])
            eigenvalues.reshape(3, 1)
            res = {'eigenvalues': eigenvalues, 'eigenvector': eigenvector}
            # print(res)
            return res
        else:
            return self.feature_matrix(matrix, dimension, eigenvector=eigenvector)


        
