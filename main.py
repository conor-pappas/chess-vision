from lib import load_position
from detect_squares import detect_lines
import plottings


def build_plot():
  fig, ax = plt.subplots()
  ax.set_xlim((0, image.shape[1]))
  ax.set_ylim((image.shape[0], 0))
  ax.set_axis_off()
  ax.set_title('Detected lines')
  return ax
  

def plot_lines(ax, lines): 
  for line in lines:
      p0, p1 = line
      ax.plot((p0[0], p1[0]), (p0[1], p1[1]))
  
position_name = 'roy_lopez_marshall_attack.png'
orig = load_position(position_name)
lines = detect_lines(canny)

ax = build_plot()
ax.imshow(orig, interpolation='nearest', cmap=plt.cm.gray)
plot_lines(ax, lines)

plt.show()
