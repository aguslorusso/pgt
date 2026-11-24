#!/bin/bash

for (( a=306; a<=2506; a+=200 ))
do
    echo 'Running next size'
    b=$((a - 200))
    bash run_DIJKred.sh 0.10 "$a" "$b"
    wait
    bash run_update.sh "$a" 0.10
    wait
done
