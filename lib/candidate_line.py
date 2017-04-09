import numpy as np

class CandidateLine:

  ANGLE_THRESHOLD = 1e-21

  def __init__(self, distance, angle):
    self.angle = angle
    self.distance = distance

  def __repr__(self):
    return '(%s, %s)' % (self.distance, self.angle)

  def __eq__(self, other):
    low_threshold = self.angle*(1 - self.ANGLE_THRESHOLD)
    high_threshold = self.angle*(1 + self.ANGLE_THRESHOLD)
    a = low_threshold <= other.angle <= high_threshold
    return a

  def __intersection_a_vector(self):
    return [self.__angle_cot(), 1]

  def __intersection_b__value(self):
    return self.distance*(self.__angle_cos() * self.__angle_cot() + self.__angle_sin())

  def __angle_sin(self): 
    return np.sin(self.angle)

  def __angle_cos(self): 
    return np.cos(self.angle)

  def __angle_cot(self): 
    return 1/np.tan(self.angle)

  def intersection_with(self, other):
    a = [self.__intersection_a_vector(), other.__intersection_a_vector()]
    b = [self.__intersection_b__value(), other.__intersection_b__value()]
    return np.linalg.solve(a,b)

