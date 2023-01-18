from constants import OPPOSITE_DIRECTION, SQUARE_STEPS, WALL, GHOST_PORT
from .Character import Character

class PacMan(Character):
  def __init__(self, grid):
    super().__init__(grid, SQUARE_STEPS // 2, SQUARE_STEPS // 2, (1, 0))

  @property
  def location(self):
    return self.col(), self.row()

  def vacant_square(self, col, row):
    return self.grid.vacant(col, row, elements=WALL + GHOST_PORT)

  def update(self):
    dx, dy = self.direction
    if self.vacant_square(self.col(2) + dx, self.row(2) + dy):
      self.x += dx
      self.y += dy

  def change_direction(self, direction):
    dx, dy = direction
    if self.vacant_square(self.col() + dx, self.row() + dy) and (self.in_square_middle() or OPPOSITE_DIRECTION[self.direction] == direction):
      self.direction = direction
      if dx == 0:
        self.x = self.col() * SQUARE_STEPS + SQUARE_STEPS // 2
      else:
        self.y = self.row() * SQUARE_STEPS + SQUARE_STEPS // 2

  def in_square_middle(self, square_border=0.15):
    x_in_middle = (self.col() + square_border) * SQUARE_STEPS < self.x < (self.col() + 1 - square_border) * SQUARE_STEPS
    y_in_middle = (self.row() + square_border) * SQUARE_STEPS < self.y < (self.row() + 1 - square_border) * SQUARE_STEPS
    return x_in_middle and y_in_middle
  