# -*- coding: UTF-8 -*-

from .matrix import Matrix
from .version import version as __version__
from .operation import *
from .specialmatrix import *
from .abnormalConditions import *

__all__ = ['matrix', 'abnormalConditions', '__version__', 'operation', 'specialmatrix', 'Matrix', 'Spmatrix',
           'Operation', 'complex']


'''
看源代码的话请直接移步到其他文件吧LOL
因为我也是第一次编写一个库，很多东西还在摸索
模块化做的不是很好，当然耦合也是
所以这个__init__.py在我视角里只是一个标识作用，虽然我知道它能对我的模块起到初始化作用，但目前来看还并未复杂到这种地步
'''




