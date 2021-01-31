import os
from os import path
import shutil
import re

def search_file(path,result):
    lists=os.listdir(path)
    for child in lists:
        chi_dir=os.path.join(path,child)
        result.append(chi_dir)
        if os.path.isdir(chi_dir):
            search_file(chi_dir,result)

def copy_file(path,output):
    tem=os.path.split(path)[1]
    out=os.path.join(output,tem)
    os.mkdir(out)   
    def copy_in_file(path,output):
        lists=os.listdir(path)
        for child in lists:
            chi_dir=os.path.join(path,child)
            if os.path.isdir(chi_dir):
                out=os.path.join(output,child)
                os.mkdir(out)
                copy_in_file(chi_dir,out)
            else:
                shutil.copy(chi_dir,output)
    copy_in_file(path,out)

def move_file(path,output):
    tem=os.path.split(path)[1]
    out=os.path.join(output,tem)
    os.mkdir(out)
    def move_in_file(path,output):
        lists=os.listdir(path)
        for child in lists:
            chi_dir=os.path.join(path,child)
            if os.path.isdir(chi_dir):
                out=os.path.join(output,child)
                os.mkdir(out)
                move_in_file(chi_dir,out)
            else:
                shutil.move(chi_dir,output)
    move_in_file(path,out)
    def del_dir(path):
        lists=os.listdir(path)
        for child in lists:
            chi_dir=os.path.join(path,child)
            if os.path.isdir(chi_dir):
                del_dir(chi_dir)
            os.removedirs(chi_dir)
    del_dir(path)


if __name__ == "__main__":
    inp=input("请输入输入：")
    oup=input("请输入输出：")
    move_file(inp,oup)
