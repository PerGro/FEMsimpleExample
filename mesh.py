class UniformityMesh:
    def __init__(self, part, ele_nums=None, size=None):
        self.name = 'UniformityMesh'
        self.nums = ele_nums
        self.size = size
        self.part = part
        self.dimension = 2
        if self.nums:
            self.__set_from_nums()
        else:
            self.__set_from_size()
        self.__set_location_vector()

    def __set_from_nums(self):
        self.nodes = []
        self.size = self.part.get_length() / self.nums
        for i in range(self.nums + 1):
            self.nodes.append(i * self.size)

    def __set_from_size(self):
        self.nodes = []
        if self.size > part.get_length():
            print('size error')
            return 0
        self.nums = int(part.get_length() / self.size)
        for i in range(self.nums + 1):
            self.nodes.append(i * self.size)

    def __set_location_vector(self):
        self.location_vector = []
        for i in range(self.nums):
            self.location_vector.append([i, i + 1])
