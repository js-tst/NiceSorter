"""
逻辑部分
"""
import glob
import os.path
import shutil
import tkinter.messagebox as tkm

import UI

# 全局变量
global space


def Arrange():
    # 获取文本框的文字
    get_text = UI.text.get('0.0', 'end')[:-1]
    # 用分号分隔输入的字符存储成数组
    file_type = get_text.split(';')
    # 获取数组长度
    type_len = len(file_type)

    # 判断文本框是否为空或空格
    global space
    for i in range(type_len):
        if file_type[i] == '' or file_type[i].isspace():
            tkm.showinfo(title='注意', message='请不要留空')
            space = True
            print("空格是", file_type[i].isspace())
            break
        else:
            space = False
            print("空格是", file_type[i].isspace())

    # 如果文本框不为空或空格才执行
    if not space:
        # 如果输入框1为空或空格则执行
        if UI.entry1_text.get() == '' or UI.entry1_text.get().isspace() is True:
            tkm.showwarning(title='警告', message='还没有选择要整理的路径')
        # 如果输入框1为空或空格则执行
        elif UI.entry2_text.get() == '' or UI.entry2_text.get().isspace() is True:
            tkm.showwarning(title='警告', message='还没有选择整理后的路径')
        else:
            if not os.path.isdir(UI.entry1_text.get()) or not os.path.isdir(UI.entry2_text.get()):
                tkm.showwarning(title='警告', message='路径不存在或可能不是一个路径')
            else:
                for j in range(type_len):
                    # 路径与要查找的扩展名
                    path = UI.entry1_text.get() + '/*.' + file_type[j]
                    glob_path = glob.glob(path)
                    print(glob_path)
                    # 如果glob_path有值
                    if glob_path:
                        if not os.path.exists(UI.entry2_text.get() + "/" + file_type[j]):
                            # 创建文件夹
                            os.mkdir(UI.entry2_text.get() + "/" + file_type[j])
                            print("cnm")
                        # 整理文件
                        for k in range(len(glob_path)):
                            print(glob_path[k])
                            shutil.move(glob_path[k], UI.entry2_text.get() + "/" + file_type[j])
                        print("oooooooo")
                    else:
                        print("tttttttt")

                # 整理完成打开整理后的文件夹并提示
                os.startfile(UI.entry2_text.get())
                tkm.showinfo(title='注意', message='整理已完成')
