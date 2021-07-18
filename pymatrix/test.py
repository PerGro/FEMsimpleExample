import tkinter as tk
from PIL import ImageTk, Image
from pymatrix import Spmatrix, Matrix, Operation
import copy

HEIGHT = 400
WIDTH = 400


class Borad(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.place(relx=0.1, rely=0.15, relheight=0.8, relwidth=0.8)
        self.widgets = []
        self.create_widgets(master)

    def create_widgets(self, master=None):
        num = 0
        for i in range(8):
            for j in range(8):
                self.widgets.append(tk.Button(master))
                self.widgets[num].place(relx=i * 1 / 8, rely=j * 1 / 8, relheight=1 / 8, relwidth=1 / 8)
                num += 1


class Body(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.master.place(relx=0.45, rely=0.05)
        background_image = tk.PhotoImage(file=r'C:\Python3\Lib\site-packages\pymatrix\head.gif')
        self.widget = tk.Label(master, image=background_image)
        self.widget.pack()


if __name__ == '__main__':
    m = Matrix([[98*5, 98*(-2), 0], [-2*98, 3*98, -98], [0, -98, 98]])
    oper = Operation()
    mr = Spmatrix().diagonal(3, 0.27)
    a = oper.mul(oper.inverse(mr), m)
    for i in range(len(a)):
        for j in range(len(a)):
            a.matrix[i][j] = round(a.matrix[i][j], 2)
    print('原始矩阵为：', a)
    find = oper.feature_matrix(a, 3, e=0.1)
    # print(oper.feature_matrix(m, 3, e=0.1))
    # print('特征矩阵：', find['eigenvector'])
    print('特征值', find['eigenvalues'])


    # vector = [[3, 4, 5]]
    # s = Spmatrix()
    # print(isinstance(s, Matrix))
    # rotation_matrix = s.rotation(3, 30, [0, 0, 1])
    # rotation_enla_list = s.rotation_enler(30, 60, 0, res=True, rounder=4)
    # m = Matrix(vector)
    # cocl = Operation()
    # res = cocl.mul(m, rotation_matrix)
    # print(rotation_enla_list)

    # ROOT = tk.Tk()
    # ROOT.title('骚雷')
    # canvas = tk.Canvas(ROOT, height=HEIGHT, width=WIDTH, bg='#dbdbdb')
    # canvas.pack()
    # root = tk.Frame(ROOT, bd=10, bg='#dbdbdb')
    # app = Borad(master=root)
    # cc = tk.Canvas(ROOT, height=30, width=30)
    # cc.place(relx=0.45, rely=0.05)
    # background_image = tk.PhotoImage(file=r'C:\Python3\Lib\site-packages\pymatrix\head.gif')
    # label = tk.Label(cc, image=background_image)
    # label.pack()
    # app.mainloop()

# if __name__ == '__main__':
#     HEIGHT = 800
#     WIDTH = 800
#
#
#     def check():
#         print("check!")
#
#
#     root = tk.Tk()
#     canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
#     canvas.pack()
#     frame = tk.Frame(root, bg='#9ff5a3', bd=10)
#     frame.place(relx=0.3, rely=0.3, relwidth=0.4, relheight=0.4)
#     button1 = tk.Button(frame, text='Hello world', command=check())
#     button2 = tk.Button(frame, text='This is tkinter')
#     button1.place(relx=0, rely=0, relheight=0.3, relwidth=0.3)
#     button2.grid(row=0, column=1)
#     label = tk.Label(frame, text='HELLO WORLD')
#     label.grid(row=1, column=0)
#     entry = tk.Entry(frame, bg='green')
#     entry.grid(row=1, column=1)
#     bottom_frame = tk.Frame(root, bg='yellow')
#     bottom_frame.place(relx=0.3, rely=0.6, relwidth=0.4, relheight=0.4)
#     root.mainloop()
