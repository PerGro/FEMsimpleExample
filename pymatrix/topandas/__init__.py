from pymatrix.topandas import topd
from pymatrix.abnormalConditions import *

__all__ = ['topd']


try:
    from pandas import DataFrame
except ImportError:
    raise PackageError('pandas')
