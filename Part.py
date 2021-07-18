class Part:
    def __init__(self, name):
        self.name = name


class Part1DBeam(Part):
    def __init__(self, name, **kwargs):
        super(Part1DBeam, self).__init__(name)
        self.__length = kwargs['length']

    def get_length(self):
        return self.__length

    def get_type(self):
        return '1D'

