from stresses import *
from Part import *
from materials import *
from mesh import *
from displacement import *
from load import *
from function import *
from pymatrix import *

class Component:
    def __init__(self, name, **kwargs):
        self.name = name
        self.__part = part = kwargs.get('part', None)
        if self.__part:
            self.__type = part.get_type()
            self.__length = part.get_length()
        self.__material = kwargs.get('materials',  None)
        self.__mesh = kwargs.get('mesh',  None)
        self.__displacement = kwargs.get('displacement',  None)
        if self.__displacement:
            self.__set_dis_array()
        self.__load = kwargs.get('load',  None)
        if self.__load:
            self.__set_load_array()
            self.__set_force_array()
        self.__shape_function = kwargs.get('shapeFunction',  None)
        if self.__shape_function:
            self.__shape_function_dot = self.__get_sfdot(self.__shape_function)

    def get_parts(self, part):
        if isinstance(part, Part.Part) is False:
            print('error class type')
            return 0
        self.__part = part
        self.__type = part.get_type()
        self.__length = part.get_length()

    def get_matrial(self, material):
        self.__material = material

    def get_mesh(self, mesh_method):
        self.__mesh = mesh_method

    def get_displacement(self, displacement):
        self.__displacement = displacement

    def get_load(self, load):
        self.__load = load
        self.__set_load_array()

    def get_shape_function(self, shape_funciton):
        self.__shape_function = shape_funciton
        self.__shape_function_dot = self.__get_sfdot(shape_funciton)

    def __get_sfdot(self, sf):
        res = []
        for func in sf:
            name, fun = func(self.__mesh.size, self.__mesh.size)
            if name == 'LINEARTWO1DUP':
                res.append(LINEARTWO1DUPDOT)
            elif name == 'LINEARTWO1DDOWN':
                res.append(LINEARTWO1DDOWNDOT)
        return res

    def __set_load_array(self):
        if self.__load['Stress'] is None:
            return 0
        stress = self.__load['Stress']
        mark_list = []
        length = self.__part.get_length()
        res = []
        for i in range(self.__mesh.nums + 1):
            mark_list.append(i * self.__mesh.size)
        for i in range(len(mark_list) - 1):
            if mark_list[i] >= stress.get_pos()[0] and stress.get_pos()[1] >= mark_list[i + 1]:
                res.append(1)
            else:
                res.append(0)
        self.__mark_list = res

    def __set_force_array(self):
        force = self.__load['Force']
        if force is None:
            return 0
        mark_list = []
        for i in range(self.__mesh.nums + 1):
            mark_list.append(i * self.__mesh.size)
        if force.get_pos() not in mark_list:
            print('Warnning: the force does not on any nodes!')
            return [0 for i in range(mark_list)]
        res = []
        for i in mark_list:
            if i == force.get_pos():
                res.append([force.get_num()])
            else:
                res.append([0])
        self.__force_list = Matrix(res)

    def __set_dis_array(self):
        dis = self.__displacement
        if dis is None:
            print('NEED DISPLACEMENT!')
            return 0
        mark_list = []
        for i in range(self.__mesh.nums + 1):
            mark_list.append(i * self.__mesh.size)
        if dis.get_pos() not in mark_list:
            print('Warnning: the displacement does not on any nodes!')
            return 0
        res = []
        for i in mark_list:
            if i == dis.get_pos():
                if dis.get_dis() == ['x']:
                    res.append([0])
            else:
                res.append([1])
        self.__dis_list = Matrix(res)

    def send_to_system(self):
        resdic = {
            'name': self.name,
            'materials': self.__material,
            'shapeFunction': self.__shape_function,
            'shapeFunctionDot': self.__shape_function_dot,
            'length': self.__part.get_length(),
            'mesh': self.__mesh,
            'displacement': self.__displacement,
            'load': self.__load,
            'marked': self.__mark_list,
            'force': self.__force_list,
            'dis': self.__dis_list
        }
        return resdic


if __name__ == '__main__':
    c = Component(3)

