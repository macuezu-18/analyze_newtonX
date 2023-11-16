#!/usr/bin/env python

import os
import sys
from sys import argv
from itertools import islice

num_list = []
filename = argv[1] # name of the file being parsed
with open(filename) as fh:
    for line in fh.readlines()[0:2]:
        num_list.append(((line.split(','))[0]))

maxnu = max(num_list)
index = num_list.index(maxnu)

replace = (" nstatdyn = "+str(index+2))

with open("control.dyn") as f:
    data = f.readlines()

data[3] = replace+'\n'

with open('control.dyn', 'w') as f:
    f.writelines(data)

f.close()

