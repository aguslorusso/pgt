#!/usr/bin/env gnuplot

set terminal pngcairo size 900,600 enhanced font 'Arial,12'
set output 'waitlnpdf_456_2.png'

set title "LJ38 network - FPT for 456 to A (1,2,3,4,5) transition"
set xlabel "Time"
set ylabel "ln(PDF)"
set key outside top right
set grid

# Define line styles with transparency or subtle lines
set style line 1 lc rgb "#001a3f" lw 3 dt 1  # deep navy
set style line 2 lc rgb "#2c3e94" lw 3 dt 1  # indigo blue
set style line 3 lc rgb "#5a30a5" lw 3 dt 1  # strong purple
set style line 4 lc rgb "#8431b9" lw 3 dt 1  # violet purple
set style line 5 lc rgb "#b03d98" lw 3 dt 1  # magenta-purple
set style line 6 lc rgb "#cc4d6f" lw 3 dt 1  # rose
set style line 7 lc rgb "#e04a3f" lw 3 dt 1  # Ferrari-approaching
set style line 8 lc rgb "#f0271a" lw 3 dt 1  # vivid Ferrari
set style line 9 lc rgb "#ff0000" lw 3 dt 1  # pure red

plot [][]\
    'FPT.testing.374.0.07/waitlnpdfAB.0.070000' using 1:2 with lines ls 9 title '0.07', \
    'FPT.testing.374.0.06/waitlnpdfAB.0.060000' using 1:2 with lines ls 5 title '0.06', \
    'FPT.testing.374.0.05/waitlnpdfAB.0.050000' using 1:2 with lines ls 1 title '0.05'
