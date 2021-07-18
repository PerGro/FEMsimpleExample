import numpy as np
from pymatrix import *
from scipy import integrate

def combineK(kMatrix, locationMatrix, size:list):
    resKMatrix = Matrix()
    resKMatrix.zeros(size[0], size[1])
    for index, sm in enumerate(kMatrix):
        for i in range(len(sm)):
            for j in range(len(sm[0])):
                resKMatrix[locationMatrix[index][i]][locationMatrix[index][j]] += sm[i][j]
    return resKMatrix

def twoNodesLocal(size):
    locationMatrix = []
    for i in range(size - 1):
        locationMatrix.append([])
        locationMatrix[i].append(i)
        locationMatrix[i].append(i + 1)
    return locationMatrix

def combineLoadMatrix(loadMatrix, locationMatrix, size: int):
    res = Matrix()
    res.zeros(size, 1)
    for index, sm in enumerate(loadMatrix):
        for i in range(len(sm)):
            res[locationMatrix[index][i]][0] += sm[i][0]
    return res

#	须将其封装于类中
# def addDisplacement(disp, Kmatrix: mat, loadMatrix: mat):
# #     row, clo = disp.disp
# #     Kmatrix.fill(0, row=row)
# #     Kmatrix[row][col] = 1
# #     loadMatrix[row][0] = disp.data
# #     try:
# #         loadMatrix[row - 1][0] -= disp.data * Kmatrix[row - 1][col]
# #         Kmatrix[row - 1][col] = 0
# #     except:
# #         pass
# #     try:
# #         loadMatrix[row + 1][0] -= disp.data * Kmatrix[row + 1][col]
# #         Kmatrid[row + 1][col] = 0
# #     except:
# #         pass


'''
class System:
    def __init__(self, components: list, config={}):
        self._config = config
        self._components = components
        self._mode = self._config['mode']
        self._n = self._config['n']
        self._element_length = self._components[0].get_length() / self._n
        self._stress = {'num': [0], 'pos': [[0, 0]]}
        self._nodes_pos = []

    def _set_nodes(self):
        pass

    def add_disp(self, data, disp):
        pass

    def add_stress(self, num, pos):
        pass

    def _check_nodes(self):
        pass


class System1dSimple(System):
    def __init__(self, components: list, config={}):
        super().__init__(components, comfig={})
        self.__length = self._element_length
        self.__func_list = ['LINEARC0FUNC']
        self.__LINEARC0FUNC = 'LINEARC0FUNC'
        self._set_nodes()

    def set_n(self, n):
        self._n = n
        self._set_nodes()

    def set_shape_func(self, func):
        if func not in self.__func_list:
            print('function can\'t find')
            return 0
        if func == 'LINEARC0FUNC':
            self.__dN1 = - 1 / self._element_length
            self.__dN2 = self._element_length
            self.__N1 = self.__N1_linear
            self.__N2 = self.__N2_linear

    def LINEARC0FUNC(self):
        return self.__LINEARC0FUNC

    def solution(self):
        self._check_nodes()
        def get_ke(x, a, b):
            return a * self._components[0].get_E(x) * b
        def __f_empty_x(x, func, up, down):
            if down <= x <= up:
                return func(x)
            else:
                return 0
        def __f_empty(x, const, up, down):
            if down <= x <= up:
                return const
            else:
                return 0
        def get_f(x, func, bx, up, down):
            return func * x * __f_empty(x, bx, up, down)
        ke = mat.zeros(2, 2)
        f = mat.zeros(2, 1)
        k_d1 = [self.__dN1, self.__dN2]
        f_d1 = [self.__N1, self.__N2]
        for i in range(2):
            for j in range(2):
                ke[i][j], err = integrate(get_ke, 0, self.__length, args=(k_d1[i], k_d1[j]))
        for i in range(2):
            f[i][0], err = integrate(get_f, 0, self.__length, args=(f_d1[i], self._stress['num'][0], self._stress['pos'][0][0], self._stress['pos'][0][1]))
        kMatrix = []
        loadMatrix = []
        for i in range(4):
            kMatrix.append(ke)
        f_temp = self.__nodes_stress_if()
        for i in range(4):
            if f_temp[i]:
                loadMatrix.append(f)
            else:
                loadMatrix.append(mat.zeros(2, 1))
        K = combineK(kMatrix, twoNodesLocal(self._n + 1), [self._n + 1, self._n + 1])
        f = combineLoadMatrix(loadMatrix, )

    def _check_nodes(self):
        for pos in self._stress['pos']:
            if pos[0] not in self._nodes_pos or pos[1] not in self._nodes_pos:
                print('error nodes set')
                return 0

    def add_stress(self, num:list, pos:list):
        self._stress['num'] = num
        self._stress['pos'] = pos

    def __nodes_stress_if(self):
        ifs = []
        for i in range(self._n):
            if self.__compare(self._nodes_pos[i], self._stress['pos'][0][0], self._stress['pos'][0][1]) and self.__compare(self._nodes_pos[i + 1], self._stress['pos'][0][0], self._stress['pos'][0][1]):
                ifs.append(1)
            else:
                ifs.append(0)
        return ifs

    def __compare(self, x, a, b):
        if a <= x <= b:
            return True
        else:
            return False

    def _set_nodes(self):
        pos = [0]
        for i in range(self._n):
            pos.append(self._element_length)
        self._nodes_pos = pos

    @staticmethod
    def __N1_linear(x, he):
        return 1 - x / he

    @staticmethod
    def __N2_linear(x, he):
        return x / he



class Component:
    def __init__(self, length:float, pos:list, E=None, **disp):
        self._length = length
        self._pos = pos

    def get_length(self):
        return self._length

    def get_pos(self):
        return self._pos


class Deam1d(Component):
    def __init__(self, length, pos=[0], E=0, **disp):
        Component.__init__(length, pos, E, **disp)
        self.__E = E

    def get_E(self, x):
        return self.__E
'''
