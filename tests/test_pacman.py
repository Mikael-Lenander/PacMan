import unittest
from math import floor
from model import PacManGrid
from constants import SQUARE_STEPS, DOWN, LEFT, RIGHT, UP
from TestHelper import TestHelper

TEST_GRID = [
  '.....X',
  'XX.XXX',
  '.....X',
  'XX.XXX',
  'P.....'
]

class TestPacman(TestHelper):

  def setUp(self):
    self.grid = PacManGrid(TEST_GRID)
    self.pacman = self.grid.pacman

  def test_pacman_hit_wall(self):
    self.configure_pacman((0, 0), RIGHT)
    self.advance_steps(4)
    self.assertClose(self.pacman.x, 4.5 * SQUARE_STEPS)
    self.advance_steps(2)
    self.assertClose(self.pacman.x, 4.5 * SQUARE_STEPS)
  
  def test_pacman_hit_border(self):
    self.configure_pacman((2, 0), DOWN)
    self.advance_steps(4)
    self.assertClose(self.pacman.y, 4.5 * SQUARE_STEPS)
    self.advance_steps(2)
    self.assertClose(self.pacman.y, 4.5 * SQUARE_STEPS)
    self.assertClose(self.pacman.x, 2.5 * SQUARE_STEPS)
  
  def test_pacman_hit_ghost_port(self):
    self.configure_pacman((5, 4), LEFT)
    self.advance_steps(4)
    self.assertClose(self.pacman.x, 1.5 * SQUARE_STEPS)
    self.advance_steps(2)
    self.assertClose(self.pacman.x, 1.5 * SQUARE_STEPS)

  def test_pacman_change_direction_down(self):
    square_border = 0.1
    square_center_width = 1 - 2 * square_border
    self.configure_pacman((0, 0), RIGHT)
    self.advance_steps(1.5 + 0.9 * square_border)
    self.pacman.change_direction(DOWN, square_border)
    self.assertEqual(self.pacman.direction, RIGHT)
    self.assertClose(self.pacman.x, SQUARE_STEPS * (2 + 0.9 * square_border))
    self.advance_steps(0.1 * square_border + 0.1 * square_center_width)
    self.pacman.change_direction(DOWN, square_border)
    self.assertEqual(self.pacman.direction, DOWN)
    self.assertClose(self.pacman.x, 2.5 * SQUARE_STEPS)
  
  def test_pacman_change_direction_left(self):
    square_border = 0.3
    square_center_width = 1 - 2 * square_border
    self.configure_pacman((2, 4), UP)
    self.advance_steps(1.5 + 1.1 * square_border + square_center_width)
    self.pacman.change_direction(LEFT, square_border)
    self.assertEqual(self.pacman.direction, UP)
    self.pacman.change_direction(DOWN, square_border)
    self.advance_steps(0.1 * square_border + 0.1 * square_center_width)
    self.pacman.change_direction(LEFT, square_border)
    self.assertEqual(self.pacman.direction, LEFT)
    self.assertClose(self.pacman.y, 2.5 * SQUARE_STEPS)

  

if __name__ == '__main__':
    unittest.main()