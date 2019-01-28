#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' multiple image file of png composed to pdf file '
import re

__author__ = 'H_DJ'

import os
import string
from PIL import Image
from reportlab.lib.pagesizes import A4, landscape
from reportlab.pdfgen import canvas
import sys


def file_name(file_dir, suffix=".jpg"):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            paths = os.path.splitext(file)
            if paths[1] == suffix:
                file_path = os.path.join(root, file)
                L.append(file_path)
    L.sort(key=numeric_compare)
    return L


def numeric_compare(x):
    xs = x.split("\\")
    index_x = re.sub("\D", "", xs[len(xs) - 1])
    return int(index_x)


# f_pdf pdf file path ,include filename
# filedir pic file path
# suffix pic file suffix examples: .jpg
def conpdf(f_pdf, filedir, suffix):
    (w, h) = landscape(A4)

    c = canvas.Canvas(f_pdf, pagesize=landscape(A4))
    fileList = file_name(filedir, suffix)

    for f in fileList:
        (xsize, ysize) = Image.open(f).size
        ratx = xsize / w
        raty = ysize / h
        ratxy = xsize / (1.0 * ysize)
        if ratx > 1:
            ratx = 0.99
        if raty > 1:
            raty = 0.99

        rat = ratx

        if ratx < raty:
            rat = raty

        widthy = h * rat
        widthx = widthy * ratxy
        posx = (w - widthx) / 2
        if posx < 0:
            posx = 0
        posy = (h - widthy) / 2
        if posy < 0:
            posy = 0
        c.drawImage(f, posx, posy, widthx, widthy)
        c.showPage()
        print("Image to pdf success!", f)
    c.save()
    print("complete!")


if __name__ == '__main__':
    conpdf("E:\\pdf\\数据结构 Java描述第二版.pdf", "E:\\pdf\\dsje2\\", ".png")
