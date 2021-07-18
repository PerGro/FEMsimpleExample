from pymatrix import Matrix


class NumMatrix(Matrix):
    def __putr(self, mat2):
        for i in range(len(mat2.matrix)):
            self.matrix[i].extend(mat2.matrix[i])

    def __putd(self, other):
        temp = list(self.matrix)
        for i in other.matrix:
            temp.append(i)
        self.matrix = tuple(temp)

    def zero(self):
        res = NumMatrix()
        res.full(2, 6, 1)
        one = NumMatrix()
        one.full(8, 2, 1)
        two = Matrix()
        two.full(8, 2, 0)
        three = one.copy
        one.__putr(two)
        one.__putr(three)
        four = res.copy
        res.__putd(one)
        res.__putd(four)
        empty = Matrix()
        empty.full(12, 1, 0)
        res.__putr(empty)
        for i in range(len(res.matrix)):
            for j in range(len(res.matrix[0])):
                if res.matrix[i][j] == 0:
                    res.matrix[i][j] = ' '
                else:
                    res.matrix[i][j] = 0
        self.matrix = res.matrix

    def one(self):
        res = NumMatrix()
        one = Matrix()
        empty = Matrix()
        res.full(12, 4, 0)
        one.full(12, 2, 1)
        empty.full(12, 1, 0)
        res.__putr(one)
        res.__putr(empty)
        for i in range(len(res.matrix)):
            for j in range(len(res.matrix[0])):
                if res.matrix[i][j] == 0:
                    res.matrix[i][j] = ' '
        self.matrix = res.matrix

    def two(self):
        res = NumMatrix()
        one = NumMatrix()
        res.full(2, 6, 2)
        one.full(3, 4, 0)
        two = Matrix()
        two.full(3, 2, 2)
        one.__putr(two)
        three = NumMatrix()
        three.full(2, 6, 2)
        four = NumMatrix()
        four.full(3, 2, 2)
        five = Matrix()
        five.full(3, 4, 0)
        four.__putr(five)
        six = NumMatrix()
        six.full(2, 6, 2)
        res.__putd(one)
        res.__putd(three)
        res.__putd(four)
        res.__putd(six)
        empty = Matrix()
        empty.full(12, 1, 0)
        res.__putr(empty)
        for i in range(len(res.matrix)):
            for j in range(len(res.matrix[0])):
                if res.matrix[i][j] == 0:
                    res.matrix[i][j] = ' '
        self.matrix = res.matrix

    def three(self):
        res = NumMatrix()
        one = NumMatrix()
        res.full(2, 6, 3)
        one.full(3, 4, 0)
        two = Matrix()
        two.full(3, 2, 3)
        one.__putr(two)
        three = NumMatrix()
        three.full(2, 6, 3)
        four = NumMatrix()
        four.full(3, 4, 0)
        five = Matrix()
        five.full(3, 2, 3)
        four.__putr(five)
        six = NumMatrix()
        six.full(2, 6, 3)
        res.__putd(one)
        res.__putd(three)
        res.__putd(four)
        res.__putd(six)
        empty = Matrix()
        empty.full(12, 1, 0)
        res.__putr(empty)
        for i in range(len(res.matrix)):
            for j in range(len(res.matrix[0])):
                if res.matrix[i][j] == 0:
                    res.matrix[i][j] = ' '
        self.matrix = res.matrix

    def four(self):
        res = NumMatrix()
        res.full(5, 2, 4)
        one = Matrix()
        one.full(5, 2, 0)
        two = res.copy
        res.__putr(one)
        res.__putr(two)
        three = NumMatrix()
        three.full(2, 6, 4)
        four = NumMatrix()
        four.full(5, 4, 0)
        five = Matrix()
        five.full(5, 2, 4)
        four.__putr(five)
        empty = Matrix()
        empty.full(12, 1, 0)
        res.__putd(three)
        res.__putd(four)
        res.__putr(empty)
        for i in range(len(res.matrix)):
            for j in range(len(res.matrix[0])):
                if res.matrix[i][j] == 0:
                    res.matrix[i][j] = ' '
        self.matrix = res.matrix

    def five(self):
        res = NumMatrix()
        one = NumMatrix()
        res.full(2, 6, 5)
        one.full(3, 2, 5)
        two = Matrix()
        two.full(3, 4, 0)
        one.__putr(two)
        three = NumMatrix()
        three.full(2, 6, 5)
        four = NumMatrix()
        four.full(3, 4, 0)
        five = Matrix()
        five.full(3, 2, 5)
        four.__putr(five)
        six = NumMatrix()
        six.full(2, 6, 5)
        res.__putd(one)
        res.__putd(three)
        res.__putd(four)
        res.__putd(six)
        empty = Matrix()
        empty.full(12, 1, 0)
        res.__putr(empty)
        for i in range(len(res.matrix)):
            for j in range(len(res.matrix[0])):
                if res.matrix[i][j] == 0:
                    res.matrix[i][j] = ' '
        self.matrix = res.matrix

    def six(self):
        res = NumMatrix()
        one = NumMatrix()
        res.full(2, 6, 6)
        one.full(3, 2, 6)
        two = Matrix()
        two.full(3, 4, 0)
        one.__putr(two)
        three = NumMatrix()
        three.full(2, 6, 6)
        four = NumMatrix()
        four.full(3, 2, 6)
        five = Matrix()
        five.full(3, 2, 6)
        temp = Matrix()
        temp.full(3, 2, 0)
        four.__putr(temp)
        four.__putr(five)
        six = NumMatrix()
        six.full(2, 6, 6)
        res.__putd(one)
        res.__putd(three)
        res.__putd(four)
        res.__putd(six)
        empty = Matrix()
        empty.full(12, 1, 0)
        res.__putr(empty)
        for i in range(len(res.matrix)):
            for j in range(len(res.matrix[0])):
                if res.matrix[i][j] == 0:
                    res.matrix[i][j] = ' '
        self.matrix = res.matrix

    def seven(self):
        res = NumMatrix()
        res.full(2, 6, 7)
        one = NumMatrix()
        one.full(10, 4, 0)
        two = Matrix()
        two.full(10, 2, 7)
        one.__putr(two)
        empty = Matrix()
        empty.full(12, 1, 0)
        res.__putd(one)
        res.__putr(empty)
        for i in range(len(res.matrix)):
            for j in range(len(res.matrix[0])):
                if res.matrix[i][j] == 0:
                    res.matrix[i][j] = ' '
        self.matrix = res.matrix

    def eight(self):
        res = NumMatrix()
        res.full(2, 6, 8)
        one = NumMatrix()
        one.full(3, 2, 8)
        two = Matrix()
        two.full(3, 2, 0)
        three = one.copy
        one.__putr(two)
        one.__putr(three)
        four = NumMatrix()
        four.full(2, 6, 8)
        five = NumMatrix()
        five.full(3, 2, 8)
        six = Matrix()
        five2 = five.copy
        six.full(3, 2, 0)
        five.__putr(six)
        five.__putr(five2)
        seven = res.copy
        res.__putd(one)
        res.__putd(four)
        res.__putd(five)
        res.__putd(seven)
        empty = Matrix()
        empty.full(12, 1, 0)
        res.__putr(empty)
        for i in range(len(res.matrix)):
            for j in range(len(res.matrix[0])):
                if res.matrix[i][j] == 0:
                    res.matrix[i][j] = ' '
        self.matrix = res.matrix

    def nine(self):
        res = NumMatrix()
        res.full(2, 6, 9)
        one = NumMatrix()
        one.full(3, 2, 9)
        two = Matrix()
        two.full(3, 2, 0)
        three = one.copy
        one.__putr(two)
        one.__putr(three)
        four = NumMatrix()
        four.full(2, 6, 9)
        five = NumMatrix()
        five.full(3, 4, 0)
        six = Matrix()
        six.full(3, 2, 9)
        five.__putr(six)
        seven = res.copy
        res.__putd(one)
        res.__putd(four)
        res.__putd(five)
        res.__putd(seven)
        empty = Matrix()
        empty.full(12, 1, 0)
        res.__putr(empty)
        for i in range(len(res.matrix)):
            for j in range(len(res.matrix[0])):
                if res.matrix[i][j] == 0:
                    res.matrix[i][j] = ' '
        self.matrix = res.matrix
