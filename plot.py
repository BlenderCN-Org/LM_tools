import pylab
from pylab import *


# can hard code by getting rid of raw_input lines and uncommenting last line


# Name of file to load 

file1 = raw_input("Name of file: ")
file = pylab.loadtxt(file1)
#file = pylab.loadtxt('cfout.txt')

var = raw_input("Enter first columm: ")
var1 = int(var)
col1 = var1
# col1 = 0 

var = raw_input("Enter second columm: ")
var2 = int(var)
col2 = var2
# col2 = 1



tot = len(file)

# My ghetto way to ensure arrays are floating point

if tot%2 == 0:
    x = arange(0,(tot/2),.5) 
    y = arange(0,(tot/2),.5)
else:
    x = arange(0,( (tot) /2)+.5,.5)
    y = arange(0,(tot/2 )+.5,.5)


# Load x and y arrays for ploting

for k in range(0,tot):
    x[k] = float(file[k][col1])
    y[k] = float(file[k][col2])


axes = plot(x,y)
#ylim([0,.01])
#xlim( [ 0 , 400000])
show() 

