import matplotlib.pyplot as plt
import numpy as np

LINE_OPTIONS=dict(linestyle='dashed', color='orange')

def imshow(ax, image):
  ax.imshow(image, interpolation='nearest', cmap=plt.cm.gray)
  ax.set_xlim((0, image.shape[1]))
  ax.set_ylim((image.shape[0], 0))
  ax.set_axis_off()

def plot_line(ax, line, image):
  if line.is_vertical():
    ax.axvline(x=line.distance, **LINE_OPTIONS)
  else:
    m = -(line.angle_cot())
    b = line._y_intercept()
    domain = np.linspace(0, image.shape[1])
    equation = lambda x: m*x + b
    ax.plot(domain, equation(domain), **LINE_OPTIONS)

def plot_lines(ax, lines, image):
  for line in lines:
    plot_line(ax, line, image)

def plot_point(ax, point):
  ax.plot(point[0], point[1], 'o', color='purple')

def plot_points(ax, points):
  x_coords = list(p[0] for p in points)
  y_coords = list(p[1] for p in points)
  ax.plot(x_coords, y_coords, 'o', color='purple')