from pymatrix.tonumpy import tonp
from pymatrix.abnormalConditions import *

__all__ = ['tonp']


try:
    import numpy
except ImportError:
    raise PackageError('numpy')
