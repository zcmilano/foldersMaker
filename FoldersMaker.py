import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilenames
import tkinter.messagebox as mbox
import os
import shutil
# 导入tkinter模块以及其中会用到的打开文件窗口和消息提示,ttk用来让控件风格与系统一致

class FoldersMaker():
    def __init__(self):
        # 初始化时，制作一个窗口，然后调用生成组件的方法
        self.win = tk.Tk()
        self.win.title('Folders Maker')
        self.win.resizable(0,0)
        self.create_widgets()

    def create_widgets(self):
        # 添加第一个标签，文字是第一步操作指令
        label_1 = tk.Label(self.win, text='STEP 1: Input the name of your experiment', height=2,font=(12))
        label_1.pack()

        # 添加文字输入框来获取实验名称
        name = tk.StringVar()
        nameEntered = ttk.Entry(self.win, width=16, textvariable=name)
        nameEntered.pack()

        # 添加第二个标签，文字是第二步操作指令
        label_2 = tk.Label(self.win, text='STEP 2: How many participants do you have?', height=2,font=(12))
        label_2.pack()

        # 添加一个Spinbox来获取被试个数，个数少的时候可以用鼠标微调
        spin = tk.Spinbox(self.win, from_=2, to=300, width=5)
        spin.pack()

        # 添加第三个标签，文字是第三步操作指令
        label_3 = tk.Label(self.win, text='STEP 3: Choose the materials of your experiment', height=2,font=(12))
        label_3.pack()

        # put_files是按钮调用的指令
        def put_files():
            fnames = askopenfilenames()
            num = int(spin.get())

            if fnames:
                for i in range(1, num+1):
                    folder = os.getcwd()+'\\{}_'.format(name.get())+'{:0>3}'.format(i) # 拼接出文件夹的名字
                    if not os.path.exists(folder):
                        os.mkdir(folder) # 如果文件夹不存在就生成
                    for item in fnames:
                        shutil.copy(item, folder) # 将文件一个个放进去
                response = mbox.askyesno(title='Good Job', message='mission completed!\nClose the software') # 循环执行完之后弹出消息提醒
                if response:
                    exit() # 点确定之后直接退出应用，但是打包exe后无法点击退出，原因暂时未知
        # 添加选择文件的按钮
        choose = ttk.Button(self.win, text='Put Files', command=put_files,)
        choose.pack()

if __name__ == '__main__':
    maker = FoldersMaker()
    maker.win.mainloop()