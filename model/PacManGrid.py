from .PacMan import PacMan
from constants import WALL, ENEMY_PORT, SNACK

class PacManGrid:

  def __init__(self, grid):
    self.grid = grid
    self.height = len(grid)
    self.width = len(grid[0])
    self.snacks = {(x, y) for y in range(self.height) for x in range(self.width) if self.grid[y][x] == SNACK}
    self.pacman = PacMan(self)

  def occupied(self, col, row, elements=WALL + ENEMY_PORT):
    return col < 0 or col >= self.width or row < 0 or row >= self.height or self.grid[row][col] in elements

  def update(self):
    self.pacman.update()
    self.snacks.discard((self.pacman.col(1), self.pacman.row(1)))

  def __getitem__(self, index):
    return self.grid[index]
  