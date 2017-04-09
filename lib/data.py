from scipy import misc

def load_position(position_name):
  return misc.imread('data/positions/%s' % position_name)