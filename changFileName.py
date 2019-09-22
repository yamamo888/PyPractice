# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 08:38:51 2019

@author: yu
"""

import glob
import os
import pdb

oldpath = os.path.join("features","nankaipickles","*.pkl")
files = glob.glob(oldpath)

# change file name
for file in files:
    dirname = os.path.dirname(file)
    filename = os.path.basename(file)
    pdb.set_trace()
    #os.rename(file, "")