from pymatrix.abnormalConditions import PackageError
from pymatrix.xlsx import xlsx

__all__ = ['xlsx']

try:
    from pandas import read_excel, read_csv
except ImportError:
    raise PackageError('pandas')
