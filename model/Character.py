from constants import SQUARE_STEPS
from math import floor

class Character:
  def __init__(self, grid, x, y, direction):
    self.grid = grid
    self.x = x
    self.y = y
    self.direction = direction
  
  def row(self, square_quarter=0):
    return floor((self.y - self.direction[1] * SQUARE_STEPS // 4 * square_quarter) / SQUARE_STEPS)
  
  def col(self, square_quarter=0):
    return floor((self.x - self.direction[0] * SQUARE_STEPS // 4  * square_quarter) / SQUARE_STEPS)