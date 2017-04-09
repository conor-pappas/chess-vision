import matplotlib.pyplot as plt
import numpy as np

def imshow(ax, image):
  ax.imshow(image, interpolation='nearest', cmap=plt.cm.gray)
  ax.set_xlim((0, image.shape[1]))
  ax.set_ylim((image.shape[0], 0))
  ax.set_axis_off()

def plot_lines(ax, lines): 
  for line in lines:
      p0, p1 = line
      ax.plot((p0[0], p1[0]), (p0[1], p1[1]))

def plot_polar(ax, height, angles, distances):
  coords = zip(angles, distances)
  for (theta, r) in coords:
    y0 = (r - 0 * np.cos(theta)) / np.sin(theta)
    y1 = (r - height * np.cos(theta)) / np.sin(theta)
    ax.plot((0, height), (y0, y1), '-r')

def plot_corners(ax, corners):
  y_corner,x_corner = zip(*corners)
  ax.plot(x_corner,y_corner,'o')