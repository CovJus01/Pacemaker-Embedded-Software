import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from struct import *
import serial
import time,threading
import sys

from serialComm import *

global count
global unpackingPattern
#yA = [12,2,4,5,6,92,45,2567,2345,23,754,3]
#yV = [12,2,4,5,6,92,45,2567,2345,23,754,3]

def signalProcess(n):
    return (n-0.5)*3.3

def serialRead():
    unpackingPattern = '<??HHHHHH??HHHHHHHH?HHffffffffffffffffffffffffffffff'
    #unpackingPattern = '<??BBffdd??ffBBBBBH?BBffffffffffffffffffffffffffffff'
    # Number of bytes recieved is 1+1+1+1+4+4+8+8+1+1+4+4+1+1+1+1+1+2+1+1+1+(30*4) = 166
    response = ser.read(157)
    response = unpack(unpackingPattern, response)
    print(response)

def egram():
    y = serialRead()
    yA = [12,2,4,5,6,92,45,2567,2345,23,754,3]
    yV = [12,2,4,5,6,92,45,2567,2345,23,754,3]
    #yA = list(map(signalProcess,y[21:51]))
    #yV = list(map(signalProcess,y[51:]))
    count += 1
    x = [(count+j) for j in range(150)]
    axs[0].cla()
    axs[1].cla()
    axs[0].set_yticks([-4,-3.5,-3.0,-2.5,-2.0,-1.5,-1.0,-0.5,0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0])
    axs[0].set_ylim(-4, 4)
    axs[1].set_yticks([-4,-3.5,-3.0,-2.5,-2.0,-1.5,-1.0,-0.5,0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0])
    axs[1].set_ylim(-4, 4)
    axs[0].grid()
    axs[1].grid()
    axs[0].set_ylabel("Amplitude(mV)")
    axs[1].set_xlabel("Time(msec)")
    axs[1].set_ylabel("Amplitude(mV)")
    axs[0].plot(x, yA, c='r', label='Artial',linewidth=3.0)
    axs[1].plot(x, yV, c='b', label='Ventricular',linewidth=3.0)
    axs[0].set_title('Atrial')
    axs[1].set_title('Ventricular')

    fig, axs = plt.subplots(2)
    animate = animation.FuncAnimation(fig, egram, interval=150)
    plt.ioff()
    time.sleep(5)
    print('im showing')
    plt.show()
    print('im quitting')
    time.sleep(2)
    plt.close("all")

######################### OLDER CODE #####################################

#import matplotlib.pyplot as plt
#import matplotlib.animation as animation
#from matplotlib import style
#from struct import *
#import serial
#import time,threading
#import sys

##pacemaker_inputs = [0, True, 30, 50, 0, 5, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
##pacemaker_inputs = [0, True, 30, 50, 0, 0.5, 0, 0.05, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
##pacemaker_inputs = [True, True, 30, 50, 0.5, 0.5, 0.05, 0.05, 0, 0, 0, 0, 70.0, 0, 0, 0, 0, 0, 0, 0, 0]


#style.use('ggplot')

#fig = plt.figure()
#fig.set_size_inches(11,6)
#ax1 = fig.add_subplot(1,1,1)
##ax2 = fig.add_subplot(2,1,2)

#x_ax = [] #time
#y1_ax = [] #amplitude
#y2_ax = []
#xtime=0

#def grab_data():
#    global xtime
#    graph_data = ser.read(24)
#    y=unpack('ddd',graph_data)    
#    if( abs(y[2])-31 < (1e-6)):
#        x_ax.append(xtime*0.005)
#        y1_ax.append(y[0])
#        y2_ax.append(y[1])
#        xtime=xtime+1
#        if len(x_ax)>100:
#            del(x_ax[0])
#            del(y1_ax[0])
#            del(y2_ax[0])
#    threading.Timer(0.001,grab_data).start() #Timer to call grab_data function every 0.001s



#def animate(i):
#    ax1.clear()
#    ax1.plot(x_ax,y1_ax,label='Atrl_Signal')
#    ax1.plot(x_ax,y2_ax,label='Vent_Signal')
#    ax1.set_xlabel('Time (s)')
#    ax1.set_ylabel('Amplitude (mV)')
#    ax1.set_ylim(bottom=-2,top=2)
#    ax1.set_title('Egram Data Visiualization')
#    ax1.legend(loc='upper right')

## grab_data()
## ani = animation.FuncAnimation(fig, animate,interval=1000)
## plt.ioff()
## time.sleep(5)
## print('im showing')
## plt.show()
## print('im quitting')
## time.sleep(2)
## plt.close("all")
