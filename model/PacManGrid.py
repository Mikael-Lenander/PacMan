from .PacMan import PacMan
from .Ghost import Ghost
from constants import WALL, GHOST, SNACK, DIRECTIONS
from math import hypot

class PacManGrid:
  def __init__(self, map):
    self.grid = map
    self.height = len(map)
    self.width = len(map[0])
    self.snacks = {(x, y) for y in range(self.height) for x in range(self.width) if self.grid[y][x] == SNACK}
    self.pacman = PacMan(self)
    self.ghosts = self.initial_ghosts_state()
    self.step_count = 0

  def update(self):
    self.pacman.update()
    self.snacks.discard((self.pacman.col(1), self.pacman.row(1)))
    for ghost in self.ghosts:
      ghost.update()
    self.step_count += 1
  
  def pacman_ghost_collision(self, character_radius):
    return any(hypot(self.pacman.x - ghost.x, self.pacman.y - ghost.y) < 2 * character_radius for ghost in self.ghosts)

  def vacant(self, col, row, elements=WALL):
    return col >= 0 and col < self.width and row >= 0 and row < self.height and self.grid[row][col] not in elements

  def is_intersection(self, col, row):
    return (self.vacant(col + 1, row) or self.vacant(col - 1, row)) and (self.vacant(col, row + 1) or self.vacant(col, row - 1)) \

  def possible_directions(self, col, row):
    return tuple((dx, dy) for dx, dy in DIRECTIONS if self.vacant(col + dx, row + dy))

  def nodes(self):
    return {(x, y) for y in range(self.height) for x in range(self.width) if self.vacant(x, y)}

  def neighbors(self, col, row):
    return {(col + dx, row + dy) for dx, dy in DIRECTIONS if self.vacant(col + dx, row + dy)}
  
  def initial_ghosts_state(self):
    return tuple(Ghost(self, x, y) for y in range(self.height) for x in range(self.width) if self.grid[y][x] == GHOST)
  
  def reset_characters(self):
    self.pacman = PacMan(self)
    self.ghosts = self.initial_ghosts_state()
    self.step_count = 0
  