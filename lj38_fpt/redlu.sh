#!/bin/bash
# this is the source minimum - we are using 3299 for this LJ38 example
# full_min_num=$1
if [ $# -lt 4 ]; then
    exho *** ERROR this script needs two arguments
    exit 1
fi

T=$1
ext=$2
extguess=$3
full_min_num=$4

echo 1 > min.B
echo ${full_min_num} >> min.B

rm -r pathdata_files
mkdir -p pathdata_files/${T}
cp {min.data,ts.data,pathdata_MASTER,pathdata_MASTER_PGT,min.A,min.B} pathdata_files/${T}
cp NGTkeeplist pathdata_files/${T}/NGTkeeplist
cd pathdata_files/${T}
sed -i "s/TEMPERATURE XXX/TEMPERATURE ${T}/g" pathdata_MASTER
sed -i "s/TEMPERATURE XXX/TEMPERATURE ${T}/g" pathdata_MASTER_PGT
cp pathdata_MASTER_PGT pathdata
PS_IPGT2 #> output
wait
mkdir -p reduced_DIJ
echo ${ext} > reduced_DIJ/NGTmap
cat mapping | head -n${ext} | awk '{print $9}' >> reduced_DIJ/NGTmap
cp min.data.new reduced_DIJ/min.data
cp ts.data.new reduced_DIJ/ts.data
cp min.A.new reduced_DIJ/min.A
cp min.B.new reduced_DIJ/min.B
cp ../../NGTmap.guess reduced_DIJ/NGTmap.guess
cp ../../eigvec* reduced_DIJ/
# Need to find new full_min_num, i.e. where the minimum is mapped to in the new system
grep " ${full_min_num} maps to new min" mapping > tmp.file
awk '{print $9}' tmp.file > tmp2.file
red_min_num=$(<tmp2.file)
echo ${red_min_num}
sed -i "s/WAITSTARTMIN XXX/WAITSTARTMIN ${red_min_num}/g" pathdata_MASTER

cp pathdata_MASTER reduced_DIJ/pathdata
cd reduced_DIJ
PS_IPGT2 #> output
wait
mkdir -p keep_files_${ext}
cp pathdata eigenvalues eigvec* NGTmap waitlnpdfAB.* keep_files_${ext}/
mkdir -p ../../../FPT.testing.${ext}.${T}
mv keep_files_${ext}/* ../../../FPT.testing.${ext}.${T}
rm -r keep_files_${ext}
cd ../../../
# done
