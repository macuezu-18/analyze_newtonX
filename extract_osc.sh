#!/bin/bash

for x in {1..20}; do python3 /home/juliana/bin/SCRIPT_OSC_NEWTONX/oscillator.py geom$x.xyz; done
for x in {1..20}; do python3 /home/juliana/bin/SCRIPT_OSC_NEWTONX/orden.py geom$x.xyz; done
