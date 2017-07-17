import itertools

class Chessboard:

  def __init__(self, lines): 
    lines.sort()
    # This groups the lines into sets of lines that have the same angle
    sets = list(list(group) for k,group in itertools.groupby(lines))
    self.__assign_line_sets(sets)

  def __assign_line_sets(self, sets):
    # TODO For now we assume that we only found two directions of lines
    self.horizontal_lines = sets[0]
    self.vertical_lines = sets[1]

  def all_intersections(self):
    line_pairs = itertools.product(self.horizontal_lines, self.vertical_lines)  
    return list(pair[0].intersection_with(pair[1]) for pair in line_pairs)