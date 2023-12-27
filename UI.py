"""
界面程序部分
"""
import tkinter as tk
import tkinter.filedialog as tkf

import Logic

# 实例化窗口对象
root = tk.Tk()
# 输入框文字
entry1_text = tk.StringVar()
entry2_text = tk.StringVar()

# 全局变量
global text


def dir_path(ent, keyword):
    # 获取文件夹路径
    ask_dir = tkf.askdirectory(title=keyword)
    # 显示在输入框上
    ent.set(ask_dir)


def UI_Init():
    # 窗口大小
    root_width = 400
    root_height = 220

    # 获取屏幕尺寸
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 窗口大小
    root.geometry("{}x{}+{}+{}".format(root_width, root_height,
                                       int((screen_width - root_width) / 2), int((screen_height - root_height) / 2))
                  )
    # 禁止改变窗口的宽与高
    root.resizable(False, False)
    # 窗口标题
    root.title("NiceSorter")

    # 按钮1
    button1 = tk.Button(root, text="选择路径", command=lambda: dir_path(entry1_text, keyword="要整理的路径"))
    # 按钮2
    button2 = tk.Button(root, text="整理", command=Logic.Arrange)
    # 按钮3
    button3 = tk.Button(root, text="选择路径", command=lambda: dir_path(entry2_text, keyword="整理后的路径"))

    # 输入框1默认文字
    entry1_text.set(value='请选择要整理的路径')
    # 输入框1
    entry1 = tk.Entry(root, textvariable=entry1_text)
    # 输入框2默认文字
    entry2_text.set(value='请选择整理后的路径')
    # 输入框2
    entry2 = tk.Entry(root, textvariable=entry2_text)

    # 标签1
    label1 = tk.Label(root, text="路径:")
    # 标签2
    label2 = tk.Label(root, text="路径:")
    # 标签3
    label3 = tk.Label(root, text="要进行整理的文件类型（扩展名，用；隔开）")
    # 标签4
    label4 = tk.Label(root, fg='#808080', text="Powered\nby\nJSTST\nA.D.\n2023-\n12-27\nver-0.1")

    # 滚动条
    text_scrollbar = tk.Scrollbar(root)

    # 文本框
    global text
    text = tk.Text(root, width=40, height=8)
    # 文本框关联滚动条
    text.config(yscrollcommand=text_scrollbar.set)
    text_scrollbar.config(command=text.yview)

    # 格式化组件
    label4.place(x=0, y=90)
    text_scrollbar.place(x=342, y=90, height=107)
    label3.pack(side='bottom')
    text.pack(side='bottom')
    entry2.place(x=58, y=58, width=244)
    button3.place(x=301, y=53)
    label2.pack(side='bottom', anchor='w', padx=(25, 0),  pady=(0, 10))
    label1.pack(side='left', padx=(25, 0))
    entry1.pack(side='left', ipadx=50)
    button1.pack(side='left')
    button2.pack(side='left', padx=(2, 0))
