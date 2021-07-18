class Load:
    def __init__(self, num, pos):
        self._num = num
        self._pos = pos

    def set_num(self, num):
        self._num = num

    def set_pos(self, pos):
        self._pos = pos

    def get_num(self):
        return self._num

    def get_pos(self):
        return self._pos


class Force(Load):
    def __init__(self, num, pos, orig=None):
        super(Force, self).__init__(num, pos)
        self.__type = 'Force'

    def get_type(self):
        return self.__type


class ForceX(Force):
    def __init__(self, num, pos):
        super(ForceX, self).__init__(num, pos)
        self.__type = 'ForceX'


class BodyStressX(Load):
    def __init__(self, num, pos):
        super(BodyStressX, self).__init__(num, pos)
        self.__type = 'BodyForce'

    def get_type(self):
        return self.__type

    def get_func(self):
        def f(x):
            return self.get_num()
        return f
