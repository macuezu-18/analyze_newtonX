#!/usr/bin/env python
# Parses MOLCAS files to extract binding energies and Dyson norms from 
# OpenMOlcas outputs. Usage: 
# python {script} argv[1](name of the file) argv[2] nº of states

import os
import sys
import numpy as np
from sys import argv
from itertools import islice

a = '* Oscillator strength for transition between'

os.path.abspath(os.getcwd())

filename = argv[1] # name of the file being parsed

osc = []
f=open(filename+str('.dat'),"w")

with open(filename) as myfile:
    for myline in myfile:
        if a in myline:
            osc = myline.split()[9]
            print(osc,file=f)
                
f.close()


