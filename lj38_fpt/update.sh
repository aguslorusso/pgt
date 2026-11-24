#!/bin/bash

ext=$1
temp=$2

rm eigvec*
cp FPT.testing.${ext}.${temp}/NGTmap NGTmap.guess
cp FPT.testing.${ext}.${temp}/eigvec* .
