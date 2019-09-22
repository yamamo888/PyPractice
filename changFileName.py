# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 08:38:51 2019

@author: yu
"""

import glob
import os
import pdb

oldpath = os.path.join("features","test","b*")
files = glob.glob(oldpath)
cnt = 2
# change file name
for file in files:
    dirname = os.path.dirname(file)
    filename = os.path.basename(file)[:-1]
    os.rename(file, filename)
    cnt += 1
