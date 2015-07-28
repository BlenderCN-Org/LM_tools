import pylab
from pylab import loadtxt

import matplotlib.pyplot as plt

file = loadtxt('MaxRe_v.txt') 
file1 = loadtxt('BL_info.txt')


x,H,x1,y = [],[],[],[]

for line in file:
	x.append( line[1] )
        H.append( line[2]/2.193 )

for line in file1:
	x1.append( line[0] )
        y.append( line[6] )

labels = ['$Re_{ \\theta}$ from $Max(Re_{v})$', '$Re_{ \\theta}$ computed directly']

plt.plot(x,H,x1,y)
plt.xlim([0.0,0.8])
plt.ylim([0.0,2000])
plt.legend(labels)
plt.grid()
plt.show() 
