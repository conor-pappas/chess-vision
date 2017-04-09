from data import load_position
from detect import detect_lines, detect_corners, hough_test
from plotting import imshow, plot_lines, plot_corners, plot_polar
import matplotlib.pyplot as plt
import skimage
  
position_name = 'roy_lopez_marshall_attack.png'
orig = skimage.transform.rotate(load_position(position_name), 1)
lines = detect_lines(orig)
corners = detect_corners(orig)

a, angles, dists = hough_test(orig)

fig, ax = plt.subplots()
imshow(ax, orig)
# plot_corners(ax, corners)
# plot_lines(ax, lines)
plot_polar(ax, orig.shape[1], angles, dists)
plt.show()
