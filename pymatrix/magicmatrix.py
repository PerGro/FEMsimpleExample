from pymatrix import Matrix
from pymatrix import Spmatrix
from pymatrix import assistfuction
from pymatrix.lib.nummatrix import NumMatrix


class MagicMatrix(Matrix):
    def __init__(self):
        super().__init__()

    def __putr(self, mat2):
        for i in range(len(mat2.matrix)):
            self.matrix[i].extend(mat2.matrix[i])

    def __putd(self, other):
        temp = list(self.matrix)
        for i in other.matrix:
            temp.append(i)
        self.matrix = tuple(temp)

    @staticmethod
    def love(num, printer=None):
        lover = MagicMatrix()
        op = assistfuction.Functions()
        one = Spmatrix()
        one.uper_ting(3, model=3)
        two = Matrix([[1], [1], [1]])
        three = Matrix([[0, 0, 0], [1, 0, 1], [1, 1, 1]])
        five = Spmatrix()
        five.uper_ting(3, model=2)
        five.T
        lover.get_matrix(op.split_matrix(one))
        lover.__putr(two)
        lover.__putr(three)
        lover.__putr(two)
        lover.__putr(five)
        add = Matrix()
        add.full(num, 11, 1)
        lover.__putd(add)
        six = Spmatrix()
        six.uper_ting(5, model=2)
        seven = Matrix([[1], [1], [1], [1], [1]])
        eight = Spmatrix()
        eight.uper_ting(5, model=1)
        eight.T
        temp2 = MagicMatrix()
        temp2.get_matrix(op.split_matrix(six))
        temp2.__putr(seven)
        temp2.__putr(eight)
        lover.__putd(temp2)
        end = Matrix([[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]])
        lover.__putd(end)
        for i in range(len(lover.matrix)):
            for j in range(len(lover.matrix[0])):
                if lover.matrix[i][j] == 0:
                    lover.matrix[i][j] = ' '
                else:
                    lover.matrix[i][j] = u'♥'
        if printer is not None:
            print('\033[31m', lover, '\033[0m')
        return lover.copy

    @staticmethod
    def draw(num, rgb=None):
        summatrix = MagicMatrix()
        summatrix.full(12, 1, ' ')
        res = NumMatrix()
        for i in str(num):
            if i == '1':
                res.one()
                summatrix.__putr(res)
            elif i == '2':
                res.two()
                summatrix.__putr(res)
            elif i == '0':
                res.zero()
                summatrix.__putr(res)
            elif i == '8':
                res.eight()
                summatrix.__putr(res)
            elif i == '9':
                res.nine()
                summatrix.__putr(res)
            elif i == '3':
                res.three()
                summatrix.__putr(res)
            elif i == '4':
                res.four()
                summatrix.__putr(res)
            elif i == '5':
                res.five()
                summatrix.__putr(res)
            elif i == '6':
                res.six()
                summatrix.__putr(res)
            elif i == '7':
                res.seven()
                summatrix.__putr(res)
        if rgb is None:
            print(summatrix)
        elif rgb == 'r':
            print('\033[31m', summatrix, '\033[0m')
        elif rgb == 'g':
            print('\033[32m', summatrix, '\033[0m')
        elif rgb == 'b':
            print('\033[34m', summatrix, '\033[0m')