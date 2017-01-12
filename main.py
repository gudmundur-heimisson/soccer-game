import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from soccer_ball import x, y
from random import random

def data_gen(t=0):
    x1, x2 = 2, 0.5
    y1, y2, y3 = -1, 1.3, 0.3
    while True:
        t += 0.05
        X, Y = x(t, x1, x2), y(t, y1, y2, y3)
        if Y < 0.1:
            y3 = Y
            y2 = 1 + random()
            t = 0
            x2 = X
            x1 = -3 + 6*random()
        yield X, Y

def init():
    ax.set_ylim(0, 1)
    ax.set_xlim(0, 1)
    del xdata[:]
    del ydata[:]
    line.set_data(xdata, ydata)
    return line,

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
ax.grid()
xdata, ydata = [], []

def run(data):
    # update the data
    X, Y = data
    xdata.append(X)
    ydata.append(Y)
    if len(xdata) >= 10:
        del xdata[:1]
        del ydata[:1]
    xmin, xmax = ax.get_xlim()
    line.set_data(xdata, ydata)
    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=False, interval=10,
                              repeat=False, init_func=init)
plt.show()
