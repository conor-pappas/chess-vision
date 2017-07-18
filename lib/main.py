from data import load_position
from detect import find_candidate_lines
from plotting import imshow, plot_points, plot_lines
from chessboard import Chessboard
import matplotlib.pyplot as plt
import skimage

  
position_name = 'roy_lopez_marshall_attack.png'
orig = skimage.transform.rotate(load_position(position_name), 0)

lines = find_candidate_lines(orig)
chessboard = Chessboard(lines)

fig, ax = plt.subplots()
imshow(ax, orig)
plot_lines(ax, lines, orig)
plot_points(ax, chessboard.all_intersections())
plt.show()