import pylab
from pylab import loadtxt

import matplotlib.pyplot as plt

file = loadtxt('MaxRe_v.txt') 


x,H,x1,y = [],[],[],[]

for line in file:
	x.append( line[1] )
        H.append( line[2] )

plt.plot(x,H)
plt.xlim([0.0,0.8])
plt.ylim([0.0,4000])
plt.show() 
