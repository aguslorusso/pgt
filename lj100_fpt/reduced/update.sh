#!/bin/bash
#cp ../dij/min.B min.B
#cat ../dij/lowest.100 > NGTkeeplist
#cat ../dij/onpath >> NGTkeeplist

PS_PI

cp min.A.new ../mfpt.reduced/min.A
cp min.B.new ../mfpt.reduced/min.B
cp min.data.new ../mfpt.reduced/min.data
cp ts.data.new ../mfpt.reduced/ts.data

echo 'copy successful!'
echo 'Initial list'
wc NGTkeeplist
echo 'Final list'
wc min.data.new
