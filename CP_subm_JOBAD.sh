#!/bin/bash

for x in {1..99}; do
    if [[ -d TRAJ${x}_CP ]]; then
	    #cp -r JOB_AD TRAJ${x}_CP/INFO_RESTART
	    #cp subm_NX.sh TRAJ${x}_CP/INFO_RESTART
	    cd TRAJ${x}_CP 
	    qsub subm_NX.sh
	    cd ..
    fi
done


