# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:46:11 2021

@author: wesva399
"""

import numpy as np
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt

#function
x = np.arange(0,10*np.pi, 0.01)
y = np.sin(2*x)

#plot figure
fig = plt.figure()
ax  = plt.subplot(1,1,1)

#how many indices to be plotted between frames
data_skip = 50

def init_func():
    ax.clear()
    plt.xlabel(r'Some variable $\varpi$')
    plt.ylabel(r'Some other variable pi')

#define animation
def update_plot(i):
    ax.plot(x[i:i+data_skip], y[i:i+data_skip], color='k')
    ax.scatter(x[i], y[i], marker='o', color = 'r')
    plt.xlim((x[0], x[-1]))
    plt.ylim(-1,1)

animation = FuncAnimation(fig,
                          update_plot,
                          frames=np.arange(0, len(x), data_skip),
                          init_func=init_func,
                          interval = 20) #minimum ms passing inbetween frames to ensure visability(might be longer though)

#animation.save('animation_wwa.mp4', dpi=150, fps=30, writer='pillow')

