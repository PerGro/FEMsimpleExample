from pymatrix.specialmatrix import Spmatrix
from pymatrix import Matrix
import random


class Game:
    def __init__(self, N):
        self.shadow = None
        self.checkerboard = None
        self.boomlist = []
        m = Matrix()
        if N == 'easy':
            m.full(8, 8, u'■')
            self.print = m.copy
            self.creat_matrix(8, 10)
        self.run()

    def init(self):
        print(self.print)

    def limit(self, x, y):
        if x < 0 or x > 7 or y < 0 or y > 7:
            return False
        else:
            return True

    def check(self):
        index = []
        for i in range(8):
            for j in range(8):
                if self.print.matrix[i][j] == ' ':
                    index.append([i, j])
        for x, y in index:
            if x + 1 < 7:
                if self.shadow.matrix[x + 2][y + 1] != 0:
                    self.print.matrix[x + 1][y] = self.shadow.matrix[x + 2][y + 1]
            if x - 1 > 0:
                if self.shadow.matrix[x][y + 1] != 0:
                    self.print.matrix[x - 1][y] = self.shadow.matrix[x][y + 1]
            if y - 1 > 0:
                if self.shadow.matrix[x + 1][y] != 0:
                    self.print.matrix[x][y - 1] = self.shadow.matrix[x + 1][y]
            if y + 1 < 7:
                if self.shadow.matrix[x + 1][y + 2] != 0:
                    self.print.matrix[x][y + 1] = self.shadow.matrix[x + 1][y + 2]

    def get_shadow(self, board):
        self.shadow = Matrix()
        self.shadow.square(len(board) + 2, full=0)
        for i in range(len(board)):
            for j in range(len(board)):
                if board.matrix[i][j] != 0:
                    for k in range(3):
                        self.shadow.matrix[i][j + k] += 1
                        self.shadow.matrix[i + 1][j + k] += 1
                        self.shadow.matrix[i + 2][j + k] += 1

    def reflash(self, point, MODEL=None):
        x, y = point
        queue = [point]
        if self.checkerboard.matrix[x][y] == 0 and MODEL is None and self.shadow.matrix[x + 1][y + 1] == 0:
            self.print.matrix[x][y] = ' '
            self.init()
            while queue:
                x, y = queue.pop(0)
                if self.limit(x + 1, y) and self.print.matrix[x + 1][y] == u'■' and self.shadow.matrix[x + 2][y + 1] == 0:
                    queue.append((x + 1, y))
                    self.print.matrix[x + 1][y] = ' ' if self.shadow.matrix[x + 2][y + 1] == 0 else self.shadow.matrix[x + 2][y + 1]
                if self.limit(x - 1, y) and self.print.matrix[x - 1][y] == u'■' and self.shadow.matrix[x][y + 1] == 0:
                    queue.append((x - 1, y))
                    self.print.matrix[x - 1][y] = ' ' if self.shadow.matrix[x][y + 1] == 0 else self.shadow.matrix[x][y + 1]
                if self.limit(x, y + 1) and self.print.matrix[x][y + 1] == u'■' and self.shadow.matrix[x + 1][y + 2] == 0:
                    queue.append((x, y + 1))
                    self.print.matrix[x][y + 1] = ' ' if self.shadow.matrix[x + 1][y + 2] == 0 else self.shadow.matrix[x + 1][y + 2]
                if self.limit(x, y - 1) and self.print.matrix[x][y - 1] == u'■' and self.shadow.matrix[x + 1][y] == 0:
                    queue.append((x, y - 1))
                    self.print.matrix[x][y - 1] = ' ' if self.shadow.matrix[x + 1][y] == 0 else self.shadow.matrix[x + 1][y]
            self.check()
            self.init()
        elif MODEL == 'over':
            self.print.matrix[x][y] = u'♂'
            self.init()
        else:
            self.print.matrix[x][y] = self.shadow.matrix[x + 1][y + 1]
            self.init()

    def draw(self, point, MODEL=None):
        return self.reflash(point, MODEL=MODEL)

    def judge(self, point):
        if point in self.boomlist:
            print('Game over!')
            self.draw(point, 'over')
            return False
        else:
            return True

    def win(self):
        num = 0
        for i in self.checkerboard:
            if i != 0:
                num += 1
        for i in self.print:
            if i == u'■':
                num -= 1
        if num == 0:
            return True
        else:
            return False

    def creat_matrix(self, de, boomnum):
        m = Matrix()
        temp = []
        for i in range(de ** 2):
            temp.append(0)
        for i in range(boomnum):
            index = random.randint(0, de ** 2 - 1)
            temp[index] = 1
        m.square(de, temp)
        self.checkerboard = m.copy

    def run(self):
        self.init()
        get_piont_r, get_piont_l = input().split(',')
        get_piont_r, get_piont_l = int(get_piont_r), int(get_piont_l)
        point = (get_piont_r, get_piont_l)
        if self.checkerboard.matrix[get_piont_r][get_piont_l] != 0:
            self.checkerboard.matrix[get_piont_r][get_piont_l] = 0
        self.get_shadow(self.checkerboard)
        for i in range(len(self.checkerboard.matrix)):
            for j in range(len(self.checkerboard.matrix[0])):
                if self.checkerboard.matrix[i][j] != 0:
                    self.boomlist.append((i, j))
        while self.judge((get_piont_r, get_piont_l)):
            if self.win():
                print('YOU WIN!')
                break
            self.reflash(point)
            get_piont_r, get_piont_l = input().split(',')
            get_piont_r, get_piont_l = int(get_piont_r), int(get_piont_l)
            point = (get_piont_r, get_piont_l)


if __name__ == '__main__':
    g = Game('easy')
