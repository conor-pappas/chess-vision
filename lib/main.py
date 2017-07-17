from data import load_position
from detect import find_chessboard
from plotting import imshow, plot_points
import matplotlib.pyplot as plt
import skimage

  
position_name = 'starting_position.png'
orig = skimage.transform.rotate(load_position(position_name), 0)

chessboard = find_chessboard(orig)

fig, ax = plt.subplots()
imshow(ax, orig)
plot_points(ax, chessboard.all_intersections())
plt.show()