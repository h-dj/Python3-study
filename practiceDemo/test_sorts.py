#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test sort function module '
import os

import re

__author__ = 'H_DJ'


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


for f in file_name("E:\\pdf\\dsje2\\", ".png"):
    print(f)
