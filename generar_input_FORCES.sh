#!/bin/bash

## SCRIPT PARA GENERAR LOS INPUTS DE LOS CALCULOS DE FORCES DE LAS DINAMICAS NEWTONX

echo '¿Has cambiado el SP.json?(si/no)'
read respuesta

if [ $respuesta == si ]; then 
	for x in *.bagel; do sed -n '1,7p' SP.json  >> "${x%.bagel}_nuevo.f" ; done
	for x in {1..100}; do cat geom"$x".bagel >> geom"$x"_nuevo.f; done
	x=1
	
	while [ $x -le 100 ]
	do 
		sed -n '26,75p' SP.json  >> geom"$x"_nuevo.f
		sed -i 's/numero/'$x'/g' geom"$x"_nuevo.f
		(( x++ ))
		echo $x
		
		if [ $x -gt 100 ]; then
			break
		fi
	done
	
	for x in {1..100}; do cp geom"$x"_nuevo.f geom"$x".json; done
	
	mkdir input_ok
	
	mv geom*.json input_ok

else
	echo 'CAMBIALO PRIMERO'
fi

