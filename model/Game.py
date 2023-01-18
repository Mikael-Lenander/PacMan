from .PacManGrid import PacManGrid
from constants import GRID

class Game:
  def __init__(self, map=GRID):
    self.grid = PacManGrid(map)
    self.lives = 3
  
  def is_lost(self):
    return self.lives == 0
  
  def is_won(self):
    return len(self.grid.snacks) == 0

  def is_over(self):
    return self.is_won() or self.is_lost()

  def is_intercepted(self, character_radius):
    return self.is_lost() or self.is_won() or self.pacman_ghost_collision(character_radius)

  def pacman_ghost_collision(self, character_radius):
    collision = self.grid.pacman_ghost_collision(character_radius)
    if collision:
      self.lives -= 1
    return collision
  
  def resume(self):
    self.grid.reset_characters()
