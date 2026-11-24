#!/bin/bash
for mina in '144'
do
	for minb in '4'
	do
		for temp in $(seq $1 $2 $3 )
		do
			all=$mina.$minb.$temp
			cp ../run.$all/reduced/eigenvalues amps.$all
		done
	done
done
		
