import numpy as np
from PyGnuplot import gp

x = np.arange(1000)/20.0
y1 = x-25
y2 = y1*np.sin(x-25)

f1 = gp()
f1.s([x, y1, y2], filename='example.out')  # save data into a file t.out
f1.c('set title "example.pdf"; set xlabel "x-axis"; set ylabel "y-axis"')
f1.c('set yrange [-25:25]; set key center top')
f1.c("plot 'example.out' u 1:2 w l t 'y=x-25")  # plot fist part
f1.c("replot 'example.out' u 1:3 w l t 'y=(x-25)*sin(x-25)'")
f1.c("replot 'example.out' u 1:(-$2) w l t 'y=25-x'")
f1.pdf('example.pdf')  # export figure into a pdf file
