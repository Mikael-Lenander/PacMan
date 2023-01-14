from constants import OPPOSITE_DIRECTION

class PacMan:
  SQUARE_STEPS = 40
  SQUARES_PER_SECOND = 3
  def __init__(self, grid):
    self.grid = grid
    self.x = self.SQUARE_STEPS // 2
    self.y = self.SQUARE_STEPS // 2
    self.direction = (1, 0)

  def row(self, square_quarter=0):
    return (self.y - self.direction[1] * self.SQUARE_STEPS // 4 * square_quarter) // self.SQUARE_STEPS
  
  def col(self, square_quarter=0):
    return (self.x - self.direction[0] * self.SQUARE_STEPS // 4  * square_quarter) // self.SQUARE_STEPS

  def update(self):
    dx, dy = self.direction
    if not self.grid.occupied(self.col(2) + dx, self.row(2) + dy):
      self.x += dx
      self.y += dy

  def change_direction(self, direction):
    dx, dy = direction
    if not self.grid.occupied(self.col() + dx, self.row() + dy) and (self.in_square_middle() or OPPOSITE_DIRECTION[self.direction] == direction):
      self.direction = direction
      if dx == 0:
        self.x = self.col() * self.SQUARE_STEPS + self.SQUARE_STEPS // 2
      else:
        self.y = self.row() * self.SQUARE_STEPS + self.SQUARE_STEPS // 2

  def in_square_middle(self, square_border=0.15):
    x_in_middle = (self.col() + square_border) * self.SQUARE_STEPS < self.x < (self.col() + 1 - square_border) * self.SQUARE_STEPS
    y_in_middle = (self.row() + square_border) * self.SQUARE_STEPS < self.y < (self.row() + 1 - square_border) * self.SQUARE_STEPS
    return x_in_middle and y_in_middle
  