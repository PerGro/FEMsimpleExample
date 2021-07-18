import math
import copy
import numpy as np


class Complex:
    def __init__(self, *args):
        self.re = None
        self.im = None
        if args:
            self.construct(args[0], args[1])

    def __repr__(self):
        print(self.re, '+', '(', self.im, ')', 'i')
        return ''

    def __len__(self):
        # res = math.sqrt(self.re ** 2 + self.im ** 2)
        return (self.re ** 2 + self.im ** 2) ** 0.5

    def __add__(self, other):
        temp = Complex()
        temp.construct(self.re, self.im)
        temp.re += other.re
        temp.im += other.im
        return temp

    def __mul__(self, other):
        temp = copy.deepcopy(self)
        res = Complex()
        res.re = temp.re * other.re - temp.im * other.im
        res.im = temp.im * other.re + temp.re * other.im
        return res

    def __sub__(self, other):
        temp = Complex()
        temp.construct(self.re, self.im)
        temp.re -= other.re
        temp.im -= other.im
        return temp

    def get_re(self):
        return self.re

    def get_im(self):
        return self.im

    def involution(self, other):
        if other is Complex():
            temp = copy.deepcopy(self)
        else:
            temp = copy.deepcopy(self)
            for _ in range(other):
                temp *= temp
        return temp

    def construct(self, re, im):
        self.re = re
        self.im = im

    def length(self):
        return (self.re ** 2 + self.im ** 2) ** 0.5


if __name__ == '__main__':
    z1 = Complex(4, 6)
    z2 = Complex(5, 3)
    print(z1 * z2)
