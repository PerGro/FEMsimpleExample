# pymatrix

此库是作者在闲余时间中抽空写出来的一个对matrix服务的库，与numpy中的matrix略有
不同，也是作者对自己的一种锻炼。

> 本库并没有经过严格的校验，如若应用到科学计算中或许会产生偏差

目录：

<a href='#Matrix'>最基本的类：Matrix</a>

<a href='#Spmatrix'>特殊矩阵：Spmatrix</a>

<a href='#operation'>运算器：Operation</a>

<a href='#Read'>读取csv: xlsx</a>

<a href='#spical'>特殊处理</a>

<a href='#abnormalConditions'>常见异常处理</a>

版本：V 1.0.1（2020/1/14更新）


<a href='#history'>历史版本及更新</a>

以下是作者的扯淡：

> 当前版本是第一个版本，也是极其相当不稳定的，部分方法逻辑上的不足与异常处理的
一团糟就足以说明问题（当然还有就是这个文档的不足也是其中之一）。不过这也是我爱好所致，
因此无法保证稳定更新，但肯定会更新的（因为我确实有可能用上这个，之前觉得创建一个矩阵太麻烦为啥不自己写一个）。
>
> 当然了，我也不认为有超过一只手能数过来的人会真正看到或是使用这个库或是这篇文档，
如果真有人用这个库或者看这篇文档了，那么
>
> 我会在以后版本会补全docstrings和优化文档的！sen mi ma sai~
>
> 日志：由于程序问题，目前将csv转换成matrix的模块运行效率相当低，这个还需在后续版本改进。
>
> 日志：由于作者本人自己的水平有限，因此很多地方无法做到与专业框架相比的条序性。
> 
> 在发布前想说的话：这是我第一次编写一个完整的“库”，很多东西还需要学习，一起进步努力吧。
>
> 若发现在使用过程中存在BUG请致信614756824@qq.com或hityourmindtg@163.com

<a name='Matrix'></a>
## Matrix

作为整个库中最基本的类，其余所有类几乎都是围绕着这个类进行工作的。在使用时要实例化
一个Matrix的对象(在10位数内都能正常打印，还是挺好看的)：

> x = pymatrix.Matrix()

每个对象都会有且只有一个矩阵来代表。若想建立两个矩阵，还需实例化一个新对象，或使用
copy()方法。每个Matrix对象所包含的矩阵遵循了numpy中的矩阵的表示方法，以元组存储。

此类的对象的迭代将是按行从上到下，从左到右依次迭代其中的值。

在获取此类对的长度（维度）时直接使用len()即可。

<a href='#1'>zeros()方法</a>&emsp;&emsp;
<a href='#2'>full()方法</a>&emsp;&emsp;
<a href='#3'>get_matrix()方法</a>&emsp;&emsp;
<a href='#copy'>copy方法(属性)</a>&emsp;&emsp;
<a href='#4'>矩阵之间的加法</a>&emsp;&emsp;

<a href='#sub'>矩阵之间的减法</a>&emsp;&emsp;
<a href='#mul'>矩阵之间的乘法</a>&emsp;&emsp;
<a href='#transposition'>矩阵转置</a>&emsp;&emsp;
<a href='#square'>square()方法</a>&emsp;&emsp;
<a href='#loc'>查找矩阵中的值</a>

<a href='#locr'>抽取矩阵中的某一行</a>&emsp;&emsp;
<a href='#locl'>抽取矩阵中的某一列</a>&emsp;&emsp;
<a href='#cut'>切片</a>&emsp;&emsp;
<a href='#reshape'>重组</a>

<a name='1'></a>
#### zeros()

该方法可以快速地建造一个n x m的值全为0的矩阵，格式为zeros(n, m):

> x.zeros(3, 4)  # 创建一个3 x 4的矩阵

其返回值为矩阵的数据形式（内部储存方式），而若print(x)则会打印其表现形式（更加
好看）。

<a name='2'></a>
#### full()

该方法算是zeros()的一个超集，所实现功能可以创造一个n x m的所有值为num的矩阵，
格式为full(n, m, num):

> x.full(3, 4, 1)  # 创建一个3 x 4并将每个值赋1

其返回值同zeros()。然而其实在这个方法中创建与赋值是同时发生的。

<a name='3'></a>
#### get_matrix()

该方法创建一个以传入参数所决定的矩阵，传入的参数必须为list类型，例如：
[[1, 2], [3, 4]]，可以创造一个2 x 2的矩阵，为：

&emsp;&emsp;1&emsp;&emsp;2

&emsp;&emsp;3&emsp;&emsp;4

特别注意：若输入的矩阵“列数”不同，例如：[1, [2, 3], 4]，则会按最高“列数”为基准，
其余空位补0处理，上述列表所创建出来的矩阵为：

&emsp;&emsp;1&emsp;&emsp;0

&emsp;&emsp;2&emsp;&emsp;3

&emsp;&emsp;4&emsp;&emsp;0

格式如下:

> x.get_matrix(list)

<a name='copy'></a>
#### copy

使用copy方法可以快速创建一个Matrix对象的拷贝，该方法被修饰为一个属性，直接调用
即可。

> x = pymatrix.Matrix()
>
> y = x.copy  # 创建了一个x的拷贝，x的所有数据被拷贝到y

<a name='4'></a>
#### 矩阵之间的加法(add)

你可以使用正常的加法来对两个尺寸相同的矩阵进行对应元素的加法：

例如，有两个矩阵a, b，他们都是Matrix的一个实例化对象，且都有相同尺寸

> c = a + b

则c为经过加法运算后的矩阵，同样也为Matrix的一个实例化对象。

<a name='sub'></a>
#### 矩阵之间的减法

同矩阵之间的加法一样，用正常的减法对两个尺寸完全相同的矩阵进行对应元素的减法。

> c = a - b  # both a and b are a object of Matrix

<a name='mul'></a>
#### 矩阵之间的乘法

如同加减法一样，直接使用便可(同时可以与一个常数进行运算)。

> c = a * b  

<a name='transposition'></a>
#### 矩阵的转置

> x.T  # x必须是一个有值的矩阵

该方法会直接对x进行转置操作，若想对原矩阵进行保留，则需要在其前面添加复制对象
（相当于是提前对x进行一次拷贝）

> y = x.copy
>
> x.T

转置方法返回的是该对象。

<a name='square'></a>
#### square()方法：

调用该方法可以创建一个n x n的矩阵：

> pymatrix.Matrix.square(n, num_list=None, full=None)

其中n参数必填，num\_list, full两个参数至少填一个：num\_list参数为一个长度不长于
n ^ 2的列表，否则超出部分将被裁剪。若只有num\_list参数，则在创建矩阵时空位用0
补齐，若同时添加num\_list与full参数，则在补空位时使用full所传递的int来补。若
只传入full参数，则创建一个所有元素值均为full的n x n矩阵。

示例：

> m = pymatrix.Matrix()
>
> m.square(3, num_list=[1,2,3,4,5])
>
> print(m)

    m:
        1   2   3
        4   5   0
        0   0   0
        
> m.square(3, num_list=[1,2,3,4,5], full=1)

    m:
        1   2   3
        4   5   1
        1   1   1
        
<a name='loc'></a>
#### 查找矩阵中的值loc()

在矩阵m：

1&emsp;&emsp;2&emsp;&emsp;3

4&emsp;&emsp;5&emsp;&emsp;6

7&emsp;&emsp;8&emsp;&emsp;9

中，使用loc方法可获得某一特定的值（需要正确的行列坐标）：

    y = m.loc(0, 1)  # y = 2
    
<a name='locr'></a>
#### 抽取矩阵的某一行locr()

格式如同loc,只需要提供正确的行数即可：

    y = m.locr(3)  # y = [7,8,9]
    
<a name='locl'></a>
#### 抽取矩阵中某一列locl()

格式如同locr,传入列数

    y = m.locl(2)  # y = [2,5,8]
    
`无论是loc还是locr或locl都不会对原矩阵造成影响`

<a name='cut'></a>
#### 切片cut()
    
使用切片方法可以快速对矩阵进行形同numpy的切片方法，但与numpy矩阵的切片略有不同。
不同于numpy该方法会直接对原矩阵进行修改，而返回修改原矩阵（省去在操作前拷贝的步骤）。


> pymatrix.Matrix.cut(rows, cols)

其中rows, cols都为不为空的列表或是一个不超过矩阵总长的int值，这里以x矩阵

1&emsp;&emsp;2&emsp;&emsp;3

4&emsp;&emsp;5&emsp;&emsp;6

7&emsp;&emsp;8&emsp;&emsp;9

矩阵为例，直接举几个例子：

    y = x.cut([0, 2], [1, 3])
    print(y)
    z = y.cut(2, 1)  # 等价于z = y.cut([2, 3], [1, 3])
    print(x)
    print(y)
    print(z)
    ans:    
        1    2    3
        4    5    6
        7    8    9
    
    
        2    3
        5    6
    
    
        8    9
    
    
        1    2    3
        4    5    6
        7    8    9
        
这样操作起来确实非常奇怪，所以在Operation中会有不对原矩阵进行切片的方法。
（因为我想保证在Matrix中所有方法是会对原矩阵产生影响的）

<a name='reshape'></a>
#### 重组

使用Matrix.reshape()可以帮助你快速通过一个list来创造一个对应n x m的矩阵，
如果此时Matrix对象已经有值，那么可以快速改变该对象的维度与列向量个数（尺寸）：

> Matrix.reshape(rows, cols, lister=None)

例如：

    from pymatrix import Matrix
    m = Matrix()
    m.reshape(4, 4, list(range(16)))
    print(m)
    m.reshape(2, 8)
    print(m)
    
    >> ans:
           0   1   2   3 
           4   5   6   7
           8   9  10  11
          12  13  14  15
          
          0   1   2   3   4   5   6   7
          8   9  10  11  12  13  14  15 
            

<a name='Spmatrix'></a>
## Spmatrix

Spmatrix是Matrix的一个子类，其主要作用是创建一些特殊矩阵来使用，正如你所见，
Matrix就像橡皮泥一样你需要自己捏成一个成像，而Spmatrix只需要输入相应的参数，
就能创建一个“预设”的矩阵。

在使用Spmatrix之前也应该创建一个它的对象，但你可以使用Matrix的方法来操作这些对象。

<a href='#sparse'>稀疏矩阵</a>&emsp;&emsp;
<a href='#uper_ting'>上三角形矩阵</a>&emsp;&emsp;
<a href='#three'>三对角矩阵</a>&emsp;&emsp;
<a href='#diagonal'>对角矩阵</a>&emsp;&emsp;
<a href='#rotation_matrix'>旋转矩阵</a>&emsp;&emsp;
<a href='#rotation_enler'>旋转矩阵——欧拉角模式</a>

<a name='sparse'></a>
#### 稀疏矩阵sparse()

你可以创造一个n x n的稀疏矩阵，稀疏矩阵的非零值为1-9的随机数字，而矩阵的稀疏程度
默认为0.9（只有不超过占比0.1的元素值为非零整数），这个参数可以自定义，
但不能低于0.7。

> sparse(n, sparse_num=0.9)

例如：

> n = pymatrix.Spmatrix()
>
> n.sparse(6)

    n:
        0   0   0   0   0   0
        0   0   0   0   0   0
        0   9   0   0   4   0
        5   1   0   0   0   0
        0   0   9   0   0   0
        0   0   0   0   0   1
        
<a name='uper_ting'></a>
#### 上三角形矩阵

> uper_ting(n, model=1)

参数：n为创造出一个n x n的矩阵，并用1来填充，model有三个参数：1， 2， 3。分别对应创造的矩阵为：

model=1(n = 3):

1&emsp;&emsp;1&emsp;&emsp;1

1&emsp;&emsp;1&emsp;&emsp;0

1&emsp;&emsp;0&emsp;&emsp;0

model=2:

1&emsp;&emsp;1&emsp;&emsp;1

0&emsp;&emsp;1&emsp;&emsp;1

0&emsp;&emsp;0&emsp;&emsp;1

model=3:

0&emsp;&emsp;0&emsp;&emsp;1

0&emsp;&emsp;1&emsp;&emsp;1

1&emsp;&emsp;1&emsp;&emsp;1

目前还无法控制斜边上的元素值，若有需要还需要一个一个修改（直接修改Matrix.matrix)。

<a name='three'></a>
#### 三对角矩阵

> Spmatrix.three_digonal(n, datalist=None)

使用该方法可以快速创建一个n x n的三对角矩阵，若传入datalist参数，则将以datalist填充非零值，
否则填充1（当datalist的长度过短时剩下的空位也会被1填充）。

所填入的n的值必须大于等于3，否则会报错。

    s1.three_digonal(3)
    s2.three_digonal(3, [1, 2, 3, 4, 5, 6, 7])
    print(s1)
    print(s2)
    
    ans:
        1    1    0
        1    1    1
        0    1    1
        
        1    2    0
        3    4    5
        0    6    7

这里实质上会修改datalist传入的参数！所以如果在后面还要用到该参数时要小心！

<a name='diagonal'></a>
#### 对角矩阵

> Spmatrix.diagonal(n, numfull=1)

使用该方法可以创建一个n x n的以数字numfull填充的对角矩阵。

<a name='rotation_matrix'></a>
#### 旋转矩阵

> Spmatrix.rotation(n, angle, vector=None)

使用该方法可以获得一个二维或三维对应旋转角为angle（弧度制）的旋转矩阵。
**若是一个三维旋转矩阵，还应传入旋转轴对应的方向向量：vector**

其中旋转的正方向遵循右手定则。

示例：

    s = Spmatrix()
    s.rotation(2, math.pi / 6)  # 获得一个旋转角为30°的旋转矩阵
    s.rotation(3, math.pi / 6, [0, 1, 0])  # 获得一个绕y轴正方向旋转30°的三维旋转矩阵。


<a name='rotation_enler'></a>
#### 旋转矩阵——欧拉角模式

> Spamtrix.rotation_enler(angle_precession, angle_nutation, angle_spin, res=False, **kwargs)
>
> angle_precession： 进动角
>
> angle_nutation: 章动角
> 
> angle_spin: 自转角
>
> 其他可填参数：z_vector:z轴单位向量坐标，默认为(0, 0, 1)， x_vector:x轴单位向量坐标，默认为(1, 0, 0)， rounder:结果保留小数位数

> 若res参数为真，返回一个Spmatrix对象（Matrix矩阵），否则返回一个由矩阵元素构成的数列。

<a name='operation'></a>
## Operation

此类承包了对于Matrix类的所有非加减乘的运算，往往你需要实例化一个此类的对象，然后
就像你用计算器一样把矩阵输入，然后得到你想要的结果，正如字面意思一样，它只是一个
计算器，他并不会对Matrix类的对象进行直接修改。

> op = pymatrix.Operation()

<a href='#mul'>矩阵乘法</a>&emsp;&emsp;
<a href='#trans'>矩阵转置</a>&emsp;&emsp;
<a href='#det'>求解行列式</a>&emsp;&emsp;
<a href='#qiepian'>矩阵的切片</a>&emsp;&emsp;
<a href='#adjoint'>矩阵的伴随矩阵</a>&emsp;&emsp;
<a href='#inverse'>矩阵的逆矩阵</a>&emsp;&emsp;
<a href='#feature_matrix'>矩阵的特征值与特征向量</a>


<a name='mul'></a>
#### 矩阵乘法

使用该方法将实现计算两个矩阵相乘的效果，其返回值为结果矩阵（Matrix对象）。

> x.get_matrix([[1, 2, 3], [4, 5, 6]])
>
> y.get_matrix([[1, 2], [3, 4], [5, 6]])
>
> res = op.mul(x, y)
>
> print(res)

得到的结果如下：

    res:
        22 28
        49 64

<a name='trans'></a>
#### 矩阵转置

> pymatrix.Operation.transposition(Matrix)

该矩阵转置与Matrix类中的转置效果一致，只不过它不会影响到被转置的矩阵，同时
返回一个结果矩阵(Matrix)。

<a name='det'></a>
#### 求解行列式

> res = determinant(mat)

将一个n x n的Matrix对象（矩阵）传入determinant，返回这个矩阵求行列式的值。

<a name='qiepian'></a>
#### cut()

使用Operation.cut()可以在不对原矩阵进行操作的情况下获得该矩阵的切片，
其参数与Matrix.cut()并无差别。

> Operation.cut(matrix, rows, cols)

同样，它返回的是一个Matrix矩阵

    x = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    y = Operation.cut(x, [0, 2], 1)
    print(x)
    print(y)
    
    ans:
        1    2    3
        4    5    6
        7    8    9
    
    
        2    3
        5    6
        
<a name='adjoint'></a>
#### 矩阵的伴随矩阵

> Operation.adjoint(mat)

使用该方法可以获得矩阵mat的一个伴随矩阵。
例：

    m = Matrix([[-2, 1], [4, -3]])  # 你当然可以使用这种方式来创建一个矩阵
    res = Operation.adjoint(m)
    print(res)
    
    ans:
        -3   -4
        -1   -2
        

<a name='inverse'></a>
#### 矩阵的逆矩阵

> Operation.inverse(mat, acc=2)

使用该方法可以获得矩阵mat的一个逆矩阵，如果它存在的话。
且所有元素的精确度默认为为小数点后两位，可以通过传入acc参数来手动修改。
例：

    m = Matrix([[-2, 1], [4, -3]])
    res = Operation.inverse(m)
    print(res)
    
    ans:
        -1.5 -0.5
        -2.0 -1.0

<a name='feature_matrix'></a>
#### 矩阵的特征值与特征向量

> Operation.feature_matrix(matrix, dimension, rou=3, theta=None, eigenvector=None, e=0.01)

其中matrix为原始矩阵，dimension为所对应的维度，rou为结果保留小数位数，e为阈值，用来控制精度，e越小，精度越大，但速度越慢。
其余参数则无需改动。

该函数的返回值为一个字典res，其中res['eigenvalue']为特征值，是一个Matrix，res['eigenvector']为特征向量，是一个Matrix。


<a name='Read'></a>
## xlsx——读取一个csv并将其中的数据转换成一个Matrix对象

在使用时务必先导入（仅仅导入pymatrix是不够的，因为其中还使用了pandas的方法）

> from pymatrix.xlsx import *

若在此之前没有安装pandas库的话，会报错并阻止pymatrix.xlsx的导入
（但不影响其他模块的使用）

<a href='#open_csv'>open\_csv</a>&emsp;&emsp;
<a href='#wirte_csv'>wirte\_csv</a>


<a name='open_csv'></a>
#### open_csv

这个方法会打开一个csv文档，然后将其转换成一个Matrix矩阵。

**注意：** 若该csv文档中的数据不是连续的，那么在空余部分会以nan填充
（就像在pandas.read_csv那样）。

> xlsx.open_csv(path, header=None, index=None, sheet_name=None)

path即为该文件的绝对地址（或相对地址，不过这里推荐使用绝对地址）
header属性则是决定是否读取表头（或将第i行作为表头读取）。

但因为Matrix没有“表头”这个概念，因此将其理解为一个“切片”也无妨。
（若header为0，则矩阵第一行对应csv文件实质上是第二行）

<a name='wirte_csv'>wirte_csv</a>
#### wirte_csv

这个方法将会将一个Matrix矩阵存放到指定目录和名字的csv文件中：

> xlsx.wirte_csv(matrix, path, name=None, header=None)

其中matrix用来传递需要写入csv的matrix矩阵，path则是csv文件保存的绝对路径。
name则是文件的名字，若不填则以当前日期（精确到秒）来命名：
例如：20200101095812.csv。
header为表头，若不填则默认为从0开始递增数列。

<a name='spical'></a>
## 特殊处理

特殊处理并没有用类封装，对应的要使用它们还必须专门导入，
因为如果你没有安装其他相关的依赖库那么你将没法正常使用这些方法。

<a href='#topandas'>将Matrix对象转换为pandas.DataFrame对象</a>&emsp;&emsp;
<a href='#tonumpy'>将Matrix对象转换为numpy.ndarry对象</a>

<a name='topandas'></a>
#### 转换为DataFrame对象

> from pymatrix.topandas import topd

先将topd方法导入，然后将想要转换的矩阵填入即可。
在填入时可以选择是否填写header属性，（表头）默认则为从0开始的递增数列。

> topd(matrix, header=None)  # return a DataFrame object

<a name='tonumpy'></a>
#### 转换为numpy.ndarry对象（numpy矩阵）

使用python进行数据分析也好，科学计算也好，总是要使用numpy来作为矩阵计算的库。
同时其他形如opency等优秀的库其主要输出对象甚至都是numpy矩阵，
因此这里也提供向numpy转换的方法。

> from pymatrix.tonumpy import tonp
>
> tonp(matrix)  # return a ndarry

<a name='abnormalConditions'></a>
## 常见异常处理

所有此库的异常：

> MatrixSizeError: 当两个矩阵不满足运算律所要求的大小时，出现此类异常
>
> MatrixTypeError：应当传入一个Matrix对象，且该对象的matrix不为空
>
> SubTypeError: 传入参数时没有成功读取到正确的参数（数据类型不对）
>
> IllegalDataError: 传入参数时没有正确填写参数（数据范围不对）

<a name='history'></a>
## 历史版本及更新内容

#### 2020/1/13 V 1.0.0：（开发周期大概有一个半月）

> pymatrix诞生
>
> 其中还有一些自己写的小东西没有在文档中写出，可以通过阅读源码来轻松获得相关信息。

#### 2020/1/14 V 1.0.1：

> 向pymatrix.xlsx.xlsx.open_csv()中添加了参数index=None与sheet_name=None，使用方法与pandas.read_excel一样。
>
> 修改了文档中时间错误的问题
>
> 修改了MagicMatrix.love()，现在可以返回一个矩阵用来储存做好的“爱心矩阵”。
>
> m = MagicMatrix.love(2)  # 在显示“爱心矩阵的同时”也将其储存到了变量m中，方便后面进行进一步操作。
>
> 但同时我去掉了自动输出的设置，若要自动输出请加入参数：love(num, printer=None)将printer改为非零即可。
>
> 在Spmatrix中新加diagonal()来创造对角矩阵。
>
> 在Spmatrix中新加rotation()来创造一个二维或三维的旋转矩阵。

#### 2020/4/3 V 1.0.5

> 更新了Spmatrix，增加了欧拉角为坐标的旋转矩阵。
>
> 更新了Operation，增加了求解特征值与特征向量的函数。