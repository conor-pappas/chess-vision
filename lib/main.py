from data import load_position
from detect import hough_peaks
from plotting import imshow, plot_lines, plot_corners, plot_polar, plot_point
import matplotlib.pyplot as plt
import skimage
from candidate_line import CandidateLine
import itertools
  
position_name = 'roy_lopez_marshall_attack.png'
orig = skimage.transform.rotate(load_position(position_name), 1)

a, angles, dists = hough_peaks(orig)
candidates = (CandidateLine(r, theta) for theta, r in zip(angles, dists))

groups = list(list(group) for k,group in itertools.groupby(candidates))
line_pairs = itertools.product(groups[0], groups[1])

fig, ax = plt.subplots()
imshow(ax, orig)
for pair in line_pairs:
  i = pair[0].intersection_with(pair[1])
  plot_point(ax, i)
plt.show()