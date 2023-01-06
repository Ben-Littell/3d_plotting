import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math
import pandas as pd
import numpy as np

x = []
y = []
z = []

for n in range(100):
    z.append(.1 * n * math.pi)
    x.append(math.cos(z[n]))
    y.append(math.sin(z[n]))


def plotscatter_3d(xd, yd, zd, plotcode='-rx'):
    fig = plt.figure(1)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xd, yd, zd, plotcode)
    plt.show()


def plot_surface_3d(xd, yd, zd):
    fig = plt.figure(1)
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(xd, yd, zd, linewidth=0, antialiased=True, color='green')
    plt.show()


# plotscatter_3d(x, y, z)

y2 = np.arange(-5, 5, 0.1)
x2 = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(x2, y2)
Z = np.exp(-(X**2 + Y**2)/2.0)

plot_surface_3d(X, Y, Z)

