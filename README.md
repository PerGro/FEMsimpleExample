# FEM Simple 1D Programmer说明

作者：中国矿业大学（北京） 力学与建筑工程学院 力学18-1 宋宜豪  学号：1810610116

## 总览

该程序作为计算力学大作业中一维问题部分的计算程序可计算在单集中应力和单均布荷载（或体力）单独或共同作用下的解答。
其中使用的第三方库分别为：

> scipy（用于计算积分）
>
> tkinter（非必需，为GUI部分）
>
> pymatrix（位于同目录下由作者自己写的矩阵运算库，没有使用到Numpy进行辅助，同时因为是纯Python编写，因此运行效率不尽人意）

*注意：由于时间紧张，故该程序能解决的问题范围相当有限，几乎是针对一维问题编写。
但可对材料进行客制化（支持非线性材料求解）。*

使用说明：

> 注：作者编写环境为Python 3.7.9，因此对3.7.9及以下版本不做兼容性保证

## 一、非GUI模式：

打开main.py文件（使用任意编辑器或记事本均可），在最后可以看到如下代码块：

    if __name__ == '__main__':
        m = Steel(1000, 0)
        p = Part1DBeam('Beam', length=10)
        mesh = UniformityMesh(p, ele_nums=4)
        dis = DOFX(0)
        load = {'Force': ForceX(25, 10), 'Stress': BodyStressX(10, [0, 5])}
        shape_function = [LINEARTWO1DUP, LINEARTWO1DDOWN]
        c = Component(
            name='test',
            part=p,
            materials=m,
            mesh=mesh,
            displacement=dis,
            load=load,
            shapeFunction=shape_function
        )
        s = System1D(c.send_to_system())
        s.solve()
    
此代码块解决的问题为C3中的例题，接下来对于一些需要设定的类进行说明：

### Steel(EX, poiss)

    m = Steel(1000, 0)
    
即表示创建了一个弹性模量为1000，泊松比为0的材料，并赋给m变量。

### Part1DBeam(name, length)

    p = Part1DBeam('Beam', length=10)
     
即表示创建了一个1DBeam模型（一维沿x正方向的“梁”），长度为10，模型名为Beam。

### UniformityMesh(part, ele_nums)

    mesh = UniformityMesh(p, ele_nums=4)

即表示设置网格为“UniformityMesh”类型的网格（对应线性二节点网格），
part参数表示要划分的模型（需要是Part及其子类，上述Part1DBeam就为Part类的一个子类），
ele_nums参数表示要划分的单元数量。

> 注意！由于作者水平有限，因此只依赖pymatrix的计算会让其在分析超过9单元问题时运行时间让人不能接受！
所以务必请使用少单元进行计算（主要问题出在对线性方程组的求解中，在main.py的124行中使用逆矩阵来求解方程组导致效率低下，
但由于时间问题作者没能将其优化，这里可以使用numpy库进行相应的修改，但要注意其中所有矩阵都为pymatrix.Matrix对象，
可通过导入pymatrix.tonumpy（具体操作可阅读pymatrix中的README.html中的特殊操作部分）将其转换为numpy.ndarry对象进行求解。）

### DOFX(pos)

    dis = DOFX(0)

此为设置约束，由于是一维问题故只会约束x方向应变为0

### ForceX(nums, pos) & BodyStressX(nums, [begin, end])

    load = {'Force': ForceX(25, 10), 'Stress': BodyStressX(10, [0, 5])}
    
需要对所有荷载进行整合，对标Force的是Force类及其子类，其中子类ForceX(nums, pos)
表示为在pos位置（起点为0）施加一个大小为nums的朝向x正向的集中力。
对标Stress的是Stress及其子类，
其中子类BodyStressX(nums, [begin, end])表示在范围为(begin, end)的区域内施加一个大小为nums,
方向为x正方向的体力（均布力）。

    shape_function = [LINEARTWO1DUP, LINEARTWO1DDOWN]    
    
这一行表示设置解决该问题的形函数，目前只提供这一类，请勿修改。

剩下的部分请不要进行修改，解决一维问题这样就足够了。

> 若有多个集中力或均布荷载作用，本程序并没有提供直接求解的方法，但根据叠加原理可分别求解最后叠加得出结果。

接下来就剩运行文件了，在命令行中输入（需将命令行定位至main.py所在目录）（或使用IDE直接运行main.py）：

    python main.py

之后在同目录下应该会生成一个根据现实时间命名的.txt文件，里面记录了**节点位移**和对应的**单元应力**。

#### 可能的报错：

1.“找不到scipy模块”，请在命令行中输入如下命令安装scipy：

    pip install scipy
    
2.“找不到pymatrix模块”，请将同目录下的pymatrix文件夹复制到Python安装目录下的lib\site-packages中

3.其他报错：请联系作者或致信614756824@qq.com

## 二、GUI模式：

运行同目录下的tk.py，之后将会看到如下界面（若没有安装tkinter库，请先安装，出现其他错误请参照上面的解决方法）

（GUI演示.png）

其中大部分选框都是“没得选”的，需要注意的有：

### Part部分

name框随便写（仅限英文），length表示1D梁的长度

### Material部分

在选择唯一的一个Material后要在新输入框中输入杨氏模量随后点击一下OK即可。

### Mesh部分

在选择Mesh后，后面填入要创建的单元数量（并非节点数量！）

### Displacement部分

Pos表示约束所在的位置

### Force部分

Pos表示集中力所在位置，Nums集中力大小

### Stress部分

Begin表示开始位置，End表示结束位置，Nums表示均布荷载大小

所有输入框全部输入数据后点击RUN，出现Output Successful提示框便表示计算成功，输出与提示所指文件，与非GUI模式下输出结果一致。
