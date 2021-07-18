import scipy
import scipy.integrate
from operation import *
from function import *
from pymatrix import *
from materials import *
from component import Component
from mesh import *
from load import *
from displacement import *
from Part import *
from stresses import *
import time


class System:
    def __init__(self, kwargs):
        self._materials = kwargs['materials']
        self._shape_function = []
        self._shape_function.extend(kwargs['shapeFunction'])
        self._shape_function_dot = []
        self._shape_function_dot.extend(kwargs['shapeFunctionDot'])
        self._mesh = kwargs['mesh']
        self._marked = kwargs['marked']
        self._load = kwargs['load']
        self._force = kwargs['force']
        self._dis = kwargs['dis']

    def __set_K_function(self):
        self.k_submatrix = []
        k_nums = self._mesh.nums
        matrix_dimension = self._mesh.dimension
        temp_m = Matrix()
        summ = []
        now_pos = 0
        for i in range(k_nums):
            temp_m.zeros(matrix_dimension, matrix_dimension)
            for row in range(matrix_dimension):
                for col in range(matrix_dimension):
                    # create load matrix
                    temp_m[row][col] = self.__get_k(self._shape_function_dot[row], self._shape_function_dot[col], self._materials.ex, now_pos)
            summ.append(temp_m.copy)
            now_pos += self._mesh.size
        combinek = combineK(summ, self._mesh.location_vector, [self._mesh.nums + 1, self._mesh.nums + 1])
        return combinek


class System1D(System):
    def __init__(self, kwargs):
        super(System1D, self).__init__(kwargs)
        self._length = kwargs['length']

    def __set_K_function(self):
        self.k_submatrix = []
        k_nums = self._mesh.nums
        matrix_dimension = self._mesh.dimension
        temp_m = Matrix()
        summ = []
        now_pos = 0
        for i in range(k_nums):
            temp_m.zeros(matrix_dimension, matrix_dimension)
            for row in range(matrix_dimension):
                for col in range(matrix_dimension):
                    # create stiffness matrix
                    temp_m[row][col] = self.__get_k(self._shape_function_dot[row], self._shape_function_dot[col], self._materials.ex, now_pos)
            summ.append(temp_m.copy)
            now_pos += self._mesh.size
        combinek = combineK(summ, self._mesh.location_vector, [self._mesh.nums + 1, self._mesh.nums + 1])
        return combinek

    # make load matrix
    def __set_F_function(self):
        f_nums = self._mesh.nums
        matrix_dimension = self._mesh.dimension
        temp_m = Matrix()
        summ = []
        now_pos = 0
        times = 0
        for i in range(f_nums):
            temp_m.zeros(matrix_dimension, 1)
            for row in range(matrix_dimension):
                temp_m[row][0] = self.__get_f(self._shape_function[row], self._load['Stress'].get_func(), now_pos) * self._marked[times]
            summ.append(temp_m.copy)
            now_pos += self._mesh.size
            times += 1
        combinef = combineLoadMatrix(summ, self._mesh.location_vector, self._mesh.nums + 1)
        return combinef

    def __add_force_to_f(self, f_list):
        temp = f_list.copy
        temp += self._force
        return temp

    def __add_dis_to_f(self, f_list):
        temp = f_list.copy
        temp *= self._dis
        return temp

    def __add_dis_to_K(self, k_matrix):
        marked = self._dis
        for i in range(len(marked)):
            if marked[i] == [0]:
                k_matrix[i][i] = 1
                for j in range(len(k_matrix[i])):
                    if j != i:
                        k_matrix[i][j] = 0
                        k_matrix[j][i] = 0
        return k_matrix

    def __get_f(self, sfd1, bx, arr):
        def tempfunc(x, he):
            _, s1 = sfd1(x, he)
            return s1 * bx(x + arr)
        var, abserr = scipy.integrate.quad(tempfunc, 0, self._mesh.size, args=(self._mesh.size, ))
        return var

    def __get_k(self, sfd1, sfd2, ef, arr):
        def tempfunc(x, he):
            return sfd1(x, he) * ef(x + arr) * sfd2(x, he)
        var, abserr = scipy.integrate.quad(tempfunc, 0, self._mesh.size, args=(self._mesh.size, ))
        return var

    def __get_ele_u(self, u):
        elements = [i for i in range(len(u) - 1)]
        pass

    def __get_ele_stress(self, u):
        elements = []
        now_points = 0
        for i in range(self._mesh.nums):
            elements.append((u[i][0] * self._shape_function_dot[1](0, self._mesh.size) + u[i + 1][0] * self._shape_function_dot[0](0, self._mesh.size)) * self._materials.ex(now_points))
            now_points += self._mesh.size
        return elements

    def solve(self, fileouput=True):
        k = self.__set_K_function()
        k = self.__add_dis_to_K(k)
        inv = Operation.inverse(k)
        f = self.__set_F_function()
        f = self.__add_force_to_f(f)
        f = self.__add_dis_to_f(f)
        u = Operation.mul(inv, f)
        stress = self.__get_ele_stress(u)
        name = str(int(time.time()))
        if fileouput:
            file = open(name + '.txt', 'w')
            file.write('Nodes strains:\n')
            file.write(str(u.matrix) + '\n')
            file.write('element stress:\n')
            file.write(str(stress) + '\n')
            file.close()
        return name



if __name__ == '__main__':
    m = Steel(1000, 0)
    p = Part1DBeam('Beam', length=58)
    mesh = UniformityMesh(p, ele_nums=8)
    dis = DOFX(0)
    load = {'Force': ForceX(25, 58), 'Stress': BodyStressX(0, [0, 0])}
    shape_function = [LINEARTWO1DUP, LINEARTWO1DDOWN]
    c = Component(
        name='test',
        part=p,
        materials=m,
        mesh=mesh,
        displacement=dis,
        load=load,
        shapeFunction=shape_function
    )
    s = System1D(c.send_to_system())
    s.solve()
