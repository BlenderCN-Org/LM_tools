import pylab
from pylab import *
import subprocess
from subprocess import Popen, PIPE
import matplotlib.pyplot as plt
matplotlib.rcParams.update({'font.size': 20})
matplotlib.rc('legend',**{'fontsize': 20})
# Name of file to load 
#file = pylab.loadtxt('bl.txt')
#tot = len(file)


cp_str = ''.join(['q.save', '\n', 'grid.in' ,'\n', 'cp.txt', '\n', str(1), 
                  '\n', str(1) , '\n', str(1), '\n', str(2)])

p1     = subprocess.Popen(['cpcalc'], stdin=PIPE, stdout=PIPE)
o1,e1  = p1.communicate(input=cp_str) 
p2     = subprocess.Popen(['tail', '-n', '+10'], stdin=PIPE, stdout=PIPE)
o2,e2  = p2.communicate(input=o1)



file = pylab.loadtxt('cp.txt')
tot = len(file) - 10

x = [.5 for i in range(tot)]
y = [.5 for i in range(tot)]

for i in range(tot):
    x[i] = file[i+10][3]
    y[i] = file[i+10][6]
    y[i] = -y[i]


plot(x,y,'k',linewidth=2)
xlim([0,1])
ylim([-1,1])
xlabel('x/c')
ylabel('$C_p$')
show()

#plot(px,dpdx)
#show()


