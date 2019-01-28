#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'H_DJ'

' 添加快捷方式，为window应用'

'''
参考
https://blog.csdn.net/MrKnight/article/details/8731356


winshell.CreateShortcut(Path, Target, Arguments="", StartIn="", Icon=("", 0), Description="")
Path – 快捷方式创建的 路径
Target – 快捷方式引用的路径
Arguments – 参数
StartIn – 那个文件夹可以用于创建快捷方式的命令
Icon – 快捷方式图标的路径
Description – 描述

1. 文件读取
- 获取文件的绝对路径

2. 运行文件时，可以手动
'''
import os

import winshell


def main():
    destDir = winshell.desktop()
    filename = "myShortcut"
    target = r"E:\Prigram_Files\360DesktopLite64.zip"

    winshell.CreateShortcut(
        Path=os.path.join(destDir, os.path.basename(filename) + ".lnk"),
        Target=target,
        Icon=(target, 0),
        Description="shortcut test")


fileList = set([]);


# 搜索指定文件
def search(path, word=''):
    for filename in os.listdir(path):
        fp = os.path.join(path, filename)
        # 如果是一个文件， 则打印文件名
        if os.path.isfile(fp) and filename.endswith(".exe"):
            print(fp[fp.rfind('\\') + 1:fp.rfind('.')])
            fileList.add(fp)
        # 否则递归继续搜索
        elif os.path.isdir(fp):
            search(fp, word)


if __name__ == "__main__":
    # main()
    # testFileAPI();
    # with open("softwareLink.properties") as sf:
    #     print(sf.read());
    search(r'E:\Prigram_Files');
    with open(file='softwareLink.properties', mode='w', encoding='utf-8') as sf:
        for filepath in list(set(fileList)):
            sf.write('{0}={1}\r'.format(filepath[filepath.rfind('\\') + 1:filepath.rfind('.')],
                                        str(filepath).replace('\\', '/')))
        sf.flush()

