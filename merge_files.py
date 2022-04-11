# coding=utf-8 
import os

result_file = "data/download.txt"


def merge_file(file_name):
    # 获取目标文件夹的路径
    filedir = os.getcwd() + '/raw_data'
    # # 获取当前文件夹中的文件名称列表  
    filenames = os.listdir(filedir)

    # # 打开当前目录下的result.txt文件，如果没有则创建
    f = open(file_name, 'a')
    # 先遍历文件名
    for filename in filenames:
        filepath = filedir + '/' + filename
        # 遍历单个文件，读取行数
        for line in open(filepath):
            f.writelines(line)
    # 关闭文件
    f.close()


if __name__ == '__main__':
    merge_file(result_file)
