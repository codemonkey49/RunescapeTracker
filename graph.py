import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
#from matplotlib import animation
import numpy as np
import time
import math
from data import *

def graph(ID):
    temp=retrieveData(ID,100)
    #print temp
    temp.reverse()
    #print temp
    plt.ion()
    for i in range (0,len(temp)):
        data=str(temp[i])
        data=data.split(",")[2]
        data=data.rstrip(")")
        #print data
        plt.scatter(i,data,c=10,s=50)
        time.sleep(0)
    plt.draw()
    plt.ylabel('some numbers')
    plt.title(ID)
    plt.show()
    plt.savefig('graph')
    
    #graph.clear()
graph(440)