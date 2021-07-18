import tkinter as tk
from main import *
from tkinter.ttk import Combobox
import tkinter.messagebox


class MainWindows:
    def __init__(self):
        self.root = tk.Tk()
        self.root.minsize(600, 200)
        self.root.title('FEM SIMPLE 1D PROGRAMMING')
        self.frame_init()
        self.label_init()
        self.label_set()
        self.button_init()
        self.button_set()
        self.combobox_init()
        self.combobox_set()
        self.entry_init()
        self.entry_set()
        self.root.mainloop()

    def __matrix_set(self):
        if self.material_combobox.get() == 'Steel':
            self.material = MiniWindowsMaterialSteel().get_mess()

    def frame_init(self):
        self.title_frame = tk.Frame(self.root, padx=5, pady=5)
        self.info_frame = tk.Frame(self.root, padx=5, pady=5)
        self.part_frame = tk.LabelFrame(self.root, text='Part', padx=5, pady=5, takefocus=True)
        # self.part_empty_frame = tk.Frame(self.part_frame, width=300)
        # self.part_empty_frame.grid(row=0, column=0)
        self.material_frame = tk.LabelFrame(self.root, text='Material', padx=5, pady=5, takefocus=True)
        self.material_left_frame = tk.Frame(self.material_frame, padx=5, pady=5, takefocus=True)
        self.material_right_frame = tk.Frame(self.material_frame, padx=5, pady=5, takefocus=True)
        self.mesh_frame = tk.LabelFrame(self.root, text='Mesh', padx=5, pady=5, takefocus=True)
        self.displacement_frame = tk.LabelFrame(self.root, text='Displacement', padx=5, pady=5, takefocus=True)
        self.load_frame = tk.LabelFrame(self.root, text='Load', padx=5, pady=5, takefocus=True)
        self.load_force_frame = tk.LabelFrame(self.load_frame, text='Froce', padx=5, pady=5, takefocus=True)
        self.load_stress_frame = tk.LabelFrame(self.load_frame, text='Stress', padx=5, pady=5, takefocus=True)
        self.shape_function_frame = tk.LabelFrame(self.root, text='Shape Function', padx=5, pady=5, takefocus=True)
        self.button_frame = tk.Frame(self.root)

        self.title_frame.pack()
        self.info_frame.pack()
        self.part_frame.pack(anchor=tk.W, padx=5)
        self.material_frame.pack(anchor=tk.W, padx=5)
        self.mesh_frame.pack(anchor=tk.W, padx=5)
        self.material_left_frame.grid(row=0, column=0)
        self.material_right_frame.grid(row=0, column=1)
        self.displacement_frame.pack(anchor=tk.W, padx=5)
        self.load_frame.pack(anchor=tk.W, padx=5)
        self.load_force_frame.pack(anchor=tk.W, padx=5)
        self.load_stress_frame.pack(anchor=tk.W, padx=5)
        self.shape_function_frame.pack(anchor=tk.W, padx=5)
        self.button_frame.pack(pady=10)

    def label_init(self):
        self.title_label = tk.Label(self.title_frame, text='FEM Simple 1D Programming', font=('微软雅黑', 15, 'bold'))
        self.info_label = tk.Label(self.info_frame, text='Auchor: Yihao Song, China University of mining and Technology (Beijing)', font=('微软雅黑', 8, 'bold'))
        self.info_label2 = tk.Label(self.info_frame, text='emil:614756824@qq.com', font=('微软雅黑', 8, 'bold'))
        self.part_label = tk.Label(self.part_frame, text='Part Type: ')
        self.part_name_label = tk.Label(self.part_frame, text='Part Name:')
        self.part_length_label = tk.Label(self.part_frame, text='Length:')
        self.material_label = tk.Label(self.material_left_frame, text='Material Type:')
        self.mesh_type_label = tk.Label(self.mesh_frame, text='Mesh Type:')
        self.mesh_nums = tk.Label(self.mesh_frame, text='Element Nums:')
        self.displacement_pos_label = tk.Label(self.displacement_frame, text='Displacement Pos:')
        self.dis_num_label = tk.Label(self.displacement_frame, text='Displacement Nums:')
        self.load_force_type_label = tk.Label(self.load_force_frame, text='Force Type:')
        self.load_force_pos_label = tk.Label(self.load_force_frame, text='Force Pos:')
        self.load_force_nums_label = tk.Label(self.load_force_frame, text='Force Nums:')
        self.load_stress_type_label = tk.Label(self.load_stress_frame, text='Stress Type:')
        self.load_stress_begin_label = tk.Label(self.load_stress_frame, text='Begin:')
        self.load_stress_end_label = tk.Label(self.load_stress_frame, text='End')
        self.load_stress_nums_label = tk.Label(self.load_stress_frame, text='Nums:')
        self.shape_function_type_label = tk.Label(self.shape_function_frame, text='Shape Function Type:')

    def label_set(self):
        self.title_label.pack(padx=5, pady=5)
        self.info_label.pack(padx=5, pady=5)
        self.info_label2.pack(padx=5, pady=5)
        self.part_label.grid(row=1, column=0, padx=5)
        self.part_name_label.grid(row=1, column=2, padx=5)
        self.part_length_label.grid(row=1, column=4)
        self.material_label.grid(row=0, column=0, padx=5)
        self.mesh_type_label.grid(row=0, column=0, padx=5)
        self.mesh_nums.grid(row=0, column=2, padx=5)
        self.displacement_pos_label.grid(row=0, column=0, padx=5)
        self.dis_num_label.grid(row=0, column=2, padx=5)
        self.load_force_type_label.grid(row=0, column=0, padx=5)
        self.load_force_pos_label.grid(row=0, column=2, padx=5)
        self.load_force_nums_label.grid(row=0, column=4, padx=5)
        self.load_stress_type_label.grid(row=0, column=0, padx=5)
        self.load_stress_begin_label.grid(row=0, column=2, padx=5)
        self.load_stress_end_label.grid(row=0, column=4, padx=5)
        self.load_stress_nums_label.grid(row=0, column=6, padx=5)
        self.shape_function_type_label.grid(row=0, column=0, padx=5)

    def button_init(self):
        # self.material_set_button = tk.Button(self.material_left_frame, text='set', command=self.__matrix_set)
        self.fucking_run = tk.Button(self.button_frame, text='RUN', command=self.__run, font=('微软雅黑', 12, 'bold'))

    def button_set(self):
        # self.material_set_button.grid(row=0, column=2, padx=10)
        self.fucking_run.pack()

    def __run(self):
        if self.material_combobox.get() == 'Steel':
            m = Steel(self.mess['ex'], self.mess['poiss'])
        if self.part_combobox.get() == 'Part1DBeam':
            p = Part1DBeam(self.part_name_entry.get(), length=float(self.part_length_entry.get()))
        if self.mesh_combobox.get() == 'UniformityMesh':
            mesh = UniformityMesh(p, ele_nums=int(self.mesh_nums_entry.get()))
        dis = DOFX(float(self.dis_pos_entry.get()))
        load = {'Force': eval(self.load_force_type_combobox.get())(float(self.load_force_nums_entry.get()), float(self.load_force_pos_entry.get())),
                'Stress': eval(self.load_stress_type_combobox.get())(float(self.load_stress_nums_entry.get()), [float(self.load_stress_begin_entry.get()), float(self.load_stress_end_entry.get())])}
        shape_function = self.shape_function_type_combobox.get()
        if shape_function == 'Linear 2 nodes':
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
        name = s.solve()
        tkinter.messagebox.showinfo('Output Successful', 'the result has been outputed to file ' + name +'.txt')

    def combobox_init(self):
        self.part_combobox = Combobox(self.part_frame, width=15, state='readonly')
        self.material_combobox = Combobox(self.material_left_frame, width=15, state='readonly')
        self.mesh_combobox = Combobox(self.mesh_frame, width=15, state='readonly')
        self.load_force_type_combobox = Combobox(self.load_force_frame, width=10, state='readonly')
        self.load_stress_type_combobox = Combobox(self.load_stress_frame, width=15, state='readonly')
        self.shape_function_type_combobox = Combobox(self.shape_function_frame, width=30, state='readonly')

    def combobox_set(self):
        self.part_combobox.grid(row=1, column=1)
        self.part_combobox['values'] = ['Part1DBeam']
        self.material_combobox.grid(row=0, column=1)
        self.material_combobox['values'] = ['Steel']
        self.mesh_combobox.grid(row=0, column=1)
        self.mesh_combobox['values'] = ['UniformityMesh']
        self.material_combobox.bind('<<ComboboxSelected>>', self.__flash_mesh)
        self.load_force_type_combobox.grid(row=0, column=1, padx=5)
        self.load_force_type_combobox['values'] = ['ForceX']
        self.load_stress_type_combobox.grid(row=0, column=1, padx=5)
        self.load_stress_type_combobox['values'] = ['BodyStressX']
        self.shape_function_type_combobox.grid(row=0, column=1, padx=5)
        self.shape_function_type_combobox['values'] = ['Linear 2 nodes']

    def __flash_mesh(self, *args):
        def done():
            self.mess = {'ex': float(entry.get()), 'poiss': 0}
        for wid in self.material_right_frame.winfo_children():
            wid.destroy()
        label = tk.Label(self.material_right_frame, text='EX:', pady=5, padx=5)
        entry = tk.Entry(self.material_right_frame, width=8)
        button = tk.Button(self.material_right_frame, text='OK', command=done)
        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        button.grid(row=0, column=2)

    def entry_init(self):
        self.part_name_entry = tk.Entry(self.part_frame, width=15)
        self.part_length_entry = tk.Entry(self.part_frame, width=10)
        self.mesh_nums_entry = tk.Entry(self.mesh_frame, width=5)
        self.dis_pos_entry = tk.Entry(self.displacement_frame, width=5)
        self.dis_num_entry = tk.Entry(self.displacement_frame, width=8, textvariable=tk.StringVar(value='0'))
        self.load_force_pos_entry = tk.Entry(self.load_force_frame, width=8)
        self.load_force_nums_entry = tk.Entry(self.load_force_frame, width=8)
        self.load_stress_begin_entry = tk.Entry(self.load_stress_frame, width=10)
        self.load_stress_end_entry = tk.Entry(self.load_stress_frame, width=10)
        self.load_stress_nums_entry = tk.Entry(self.load_stress_frame, width=10)

    def entry_set(self):
        self.part_name_entry.grid(row=1, column=3, padx=5)
        self.part_length_entry.grid(row=1, column=7, padx=5)
        self.mesh_nums_entry.grid(row=0, column=3, padx=5)
        self.dis_pos_entry.grid(row=0, column=1, padx=5)
        self.dis_num_entry.grid(row=0, column=3)
        self.dis_num_entry.config(state='readonly')
        self.load_force_pos_entry.grid(row=0, column=3, padx=5)
        self.load_force_nums_entry.grid(row=0, column=5, padx=5)
        self.load_stress_begin_entry.grid(row=0, column=3, padx=5)
        self.load_stress_end_entry.grid(row=0, column=5, padx=5)
        self.load_stress_nums_entry.grid(row=0, column=7, padx=5)


        class MiniWindowsMaterialSteel:
            def __init__(self):
                self.root = tk.Tk()
                self.root.minsize(80, 40)
                self.label = tk.Label(self.root, text='EX:', pady=5, padx=5)
                self.entry = tk.Entry(self.root, width=8)
                self.button = tk.Button(self.root, text='OK', command=self.done)
                self.label.grid(row=0, column=0)
                self.entry.grid(row=0, column=1)
                self.button.grid(row=0, column=2)
                self.root.mainloop()

            def done(self):
                self.mess = {'ex': float(self.entry.get()), 'poiss': 0}
                self.root.destroy()

            def get_mess(self):
                return self.mess


if __name__ == '__main__':
    m = MainWindows()
