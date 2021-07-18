class MatrixSizeError(Exception):
    def __init__(self, size=None):
        self.size = size

    def __str__(self):
        return 'the matrix should be same or right size: {}'.format(self.size)


class MatrixTypeError(Exception):
    def __str__(self):
        return 'input must be a matrix'


class SubTypeError(Exception):
    def __init__(self, types):
        self.type = types

    def __str__(self):
        return 'it must be a {}'.format(self.type)


class IllegalDataError(Exception):
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return 'illegal data entered, should be {}'.format(self.info)


class PackageError(Exception):
    def __init__(self, error):
        self.error = error

    def __str__(self):
        return 'install {} at first'.format(self.error)
