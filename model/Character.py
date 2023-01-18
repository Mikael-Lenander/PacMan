from constants import SQUARE_STEPS
from math import floor

class Character:
  def __init__(self, grid, col, row, direction):
    self.grid = grid
    self.setLocation(col, row)
    self.direction = direction
  
  def row(self, square_quarter=0):
    return floor((self.y - self.direction[1] * SQUARE_STEPS // 4 * square_quarter) / SQUARE_STEPS)
  
  def col(self, square_quarter=0):
    return floor((self.x - self.direction[0] * SQUARE_STEPS // 4  * square_quarter) / SQUARE_STEPS)

  @property
  def location(self):
    return self.col(), self.row()

  def setLocation(self, col, row):
    self.x = col * SQUARE_STEPS + SQUARE_STEPS // 2
    self.y = row * SQUARE_STEPS + SQUARE_STEPS // 2

  def center_sideways(self, direction):
    if direction[0] == 0:
      self.x = self.col() * SQUARE_STEPS + SQUARE_STEPS // 2
    else:
      self.y = self.row() * SQUARE_STEPS + SQUARE_STEPS // 2