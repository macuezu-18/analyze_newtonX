#!/bin/bash

touch oo
echo ETOT_DRIFT = 0.75 >> oo
echo ETOT_JUMP = 0.75 >> oo
echo / >> oo

for x in {1..100}; do
    if [[ -d TRAJ${x}_CP ]]; then
        if [[ -f TRAJ${x}_CP/control.dyn ]]; then
            cp oo TRAJ${x}_CP
            sed -n '1,10p' TRAJ${x}_CP/control.dyn  > temp
            cat oo >> temp
            cp temp TRAJ${x}_CP/control.dyn
            rm temp
	    rm oo
        fi
    fi
done


