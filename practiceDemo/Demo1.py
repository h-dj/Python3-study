#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn.externals import joblib

' a test module '

__author__ = 'H_DJ'

copyrf = joblib.load(r'C:\Users\hdj\Desktop\model\rf7.pkl')
print(str(copyrf))
