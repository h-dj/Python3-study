#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'H_DJ'

# 往pdf文件中添加书签
from PyPDF2 import PdfFileReader as reader, PdfFileWriter as writer

import sys

pageIndex = [1, 1, 1, 4, 4, 5, 9, 10, 12, 12, 13, 14, 20, 23, 25,
             26, 29, 29, 29, 30, 31, 31, 33, 36, 37, 38, 40, 47, 50,
             55, 56, 63, 63, 66, 66, 66, 67, 67, 70, 73, 85, 85,
             86, 86, 90, 92, 94, 98, 100, 103, 104, 107, 107, 107,
             108, 109, 109, 109, 110, 110, 112, 115, 115, 117, 122,
             128, 129, 129, 130, 131, 131, 132, 132, 133, 133, 139, 141,
             142, 143, 146, 146, 149, 149, 151, 153, 156, 156, 163,
             168, 173, 173, 174, 177, 179, 179, 182, 185, 187, 188,
             190, 190, 190, 194, 194, 195, 200, 205, 206, 208, 209,
             215, 215, 216, 217, 220, 221, 223, 227, 228, 228, 230,
             234, 235, 238, 238, 241, 241, 244, 245, 245, 247, 250,
             250, 251, 255, 260, 263, 263, 263, 266, 267, 269, 269,
             271, 271, 272, 273, 277, 280, 282, 285, 285, 286, 286, 287,
             289, 292, 292, 299, 302, 311, 313, 313, 314, 317,
             322, 323, 324, 327, 390]


def getPageMark():
    pageMark = []
    with open("E:\\pdf\\数据结构 Java描述第二版 目录.txt", 'r', encoding='utf-8') as file:
        for line in file:
            pageMark.append(line.strip('\n\t\ufeff'))
    return pageMark


def main():
    # 读取PDF文件，创建PdfFileReader对象
    book = reader('E:/pdf/数据结构 Java描述第二版.pdf')

    # 创建PdfFileWriter对象，并用拷贝reader对象进行初始化
    pdf = writer()
    pdf.cloneDocumentFromReader(book)

    # 添加书签
    # 注意：页数是从0开始的，中文要用unicode字符串，否则会出现乱码
    # 如果这里的页码超过文档的最大页数，会报IndexError异常
    marks = getPageMark()
    for mark, index in zip(marks, pageIndex):
        pdf.addBookmark(mark, index + 12)

    # 保存修改后的PDF文件内容到文件中
    # 注意：这里必须用二进制的'wb'模式来写文件，否则写到文件中的内容都为乱码
    with open('E:/pdf/数据结构 Java描述第二版(new).pdf', 'wb') as fout:
        pdf.write(fout)


if __name__ == '__main__':
    main()
