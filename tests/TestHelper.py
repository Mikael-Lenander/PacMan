import unittest
from math import floor
from constants import SQUARE_STEPS

class TestHelper(unittest.TestCase):

  def assertClose(self, x, y):
    self.assertAlmostEqual(x, y, delta=1)
  
  def advance_steps(self, steps):
    for _ in range(floor(steps * SQUARE_STEPS)):
      self.grid.update()
  
  def configure_pacman(self, location, direction):
    self.pacman = self.grid.pacman
    self.pacman.direction = direction
    self.pacman.setLocation(*location)

  def assertXAndY(self, target, x, y):
    self.assertClose(target.x, x)
    self.assertClose(target.y, y)