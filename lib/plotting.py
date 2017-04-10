import matplotlib.pyplot as plt
import numpy as np

def imshow(ax, image):
  ax.imshow(image, interpolation='nearest', cmap=plt.cm.gray)
  ax.set_xlim((0, image.shape[1]))
  ax.set_ylim((image.shape[0], 0))
  ax.set_axis_off()

def plot_point(ax, point):
  ax.plot(point[0], point[1], 'o')

def plot_points(ax, points):
  x_coords = list(p[0] for p in points)
  y_coords = list(p[1] for p in points)
  ax.plot(x_coords, y_coords, 'o')