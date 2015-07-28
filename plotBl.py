import pylab
from pylab import loadtxt

import matplotlib.pyplot as plt

file = loadtxt('BL_info.txt') 


x,H,x1,y = [],[],[],[]

for line in file:
	x.append( line[0] )
        H.append( line[6] )

plt.plot(x,H)
plt.xlim([0.0,0.8])
plt.ylim([0.0,3500])
plt.show() 
