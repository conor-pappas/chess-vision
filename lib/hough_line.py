import numpy as np

class HoughLine:

  ANGLE_THRESHOLD = 1e-21

  def __init__(self, distance, angle):
    self.angle = angle
    self.distance = distance

  def __repr__(self):
    return '(%s, %s)' % (self.distance, self.angle * 180/np.pi)

  def __eq__(self, other):
    low_threshold = self.angle*(1 - self.ANGLE_THRESHOLD)
    high_threshold = self.angle*(1 + self.ANGLE_THRESHOLD)
    a = low_threshold <= other.angle <= high_threshold
    return a

  def __lt__(self, other):
    return self.angle < other.angle

  def _y_intercept(self):
    return self.distance*(self.angle_cos() * self.angle_cot() + self.angle_sin())

  def angle_sin(self): 
    return np.sin(self.angle)

  def angle_cos(self): 
    return np.cos(self.angle)

  def angle_cot(self): 
    return 1/np.tan(self.angle)

  def is_vertical(self): 
    return self.angle_sin() == 0.0

  def intersection_with(self, other):
    # If either of the lines are vertical, the equations are degenerate and require
    # a different solution.
    if self.is_vertical():
      y_coord = other._y_intercept() - (other.angle_cot() * self.distance)
      return (self.distance, y_coord)
    elif other.is_vertical():
      # We can swap the arguments to get to the code path of the first conditional
      return other.intersection_with(self)
    # Otherwise, we can just solve the matrix
    else:
      a = [[self.angle_cot(),1],[other.angle_cot(), 1]]
      b = [self._y_intercept(), other._y_intercept()]
      return np.linalg.solve(a,b) 

