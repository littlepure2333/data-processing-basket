# encoding: utf-8

import os

path_list = list()

def get_path(path, suffix_name, *args):
    """深度遍历获取所有后缀名为suffix_name的文件列表，可接收多个后缀名"""
    # 获取当前目录下的所有文件
    dir_list = os.listdir(path)
    # print(dir_list)
    for file in dir_list:
        # 遍历所有文件
        # print(os.path.abspath(path))
        # print(file)
        # 将文件绝对路径和文件名拼接
        file_path = os.path.join(os.path.abspath(path), file)
        # print(file_path)
        if os.path.isdir(file_path):
            # 若当前文件为文件夹，重新遍历当前文件夹
            print('deep in "{}"'.format(file_path))
            get_path(file_path, suffix_name, *args)
        else:
            if file_path.endswith(suffix_name):
                # 若文件后缀名为suffix_name则存储文件绝对路径
                    path_list.append(file_path)

            if len(args):
                # 若查找多个后缀名的文件，遍历需要查询的文件后缀
                for arg in args:
                    if file_path.endswith(arg):
                        # 若找到文件后缀为arg的存储文件的绝对路径
                        path_list.append(file_path)
    # print(path_list)

if __name__ == "__main__":

    # 得到所有json文件
    get_path("G:/imageFiles/downtown_walkBridge_01", "json")
    # print(path_list)

    




