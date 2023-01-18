import unittest
from model import PacManGrid, Ghost
from TestHelper import TestHelper
from constants import SQUARE_STEPS, LEFT, RIGHT, UP, DOWN

TEST_GRID_1 = [
  '.....',
  'XXXX.',
  'GXXX.',
  '.....',
]

TEST_GRID_2 = [
  '...G...',
  '.XXXX.X',
  '.XXXX.X',
  '.XXXX.X',
  '.......'
]

TEST_GRID_3 = [
  '..............',
  '..XXXXX.XXXXX.',
  '..XXXXX.XXXXX.',
  '.XXXXXX.XG.XX.',
  'G.X...X.X.....',
  '..............'
]

class GhostTest(TestHelper):
  
  def setUp(self):
    Ghost.BEST_DIRECTION_PROBABILITY = 1
    Ghost.SLOW_DOWN_FACTOR = 2
  
  def assertGhostLocations(self, upper_ghost_location, lower_ghost_location):
    self.assertEqual(self.upper_ghost.location, upper_ghost_location)
    self.assertEqual(self.lower_ghost.location, lower_ghost_location)

  def assertBasicGhostMovement(self, slow_down_factor):
    self.grid = PacManGrid(TEST_GRID_1)
    self.configure_pacman((0, 0), LEFT)
    self.ghost = self.grid.ghosts[0]
    self.advance_steps(1 * slow_down_factor)
    self.assertXAndY(self.ghost, 0.5 * SQUARE_STEPS, 3.5 * SQUARE_STEPS)
    self.advance_steps(4 * slow_down_factor)
    self.assertXAndY(self.ghost, 4.5 * SQUARE_STEPS, 3.5 * SQUARE_STEPS)
    self.advance_steps(3 * slow_down_factor)
    self.assertXAndY(self.ghost, 4.5 * SQUARE_STEPS, 0.5 * SQUARE_STEPS)
    self.advance_steps(4 * slow_down_factor)
    self.assertXAndY(self.ghost, 0.5 * SQUARE_STEPS, 0.5 * SQUARE_STEPS)

  def test_ghost_basic_movement(self):
    self.assertBasicGhostMovement(Ghost.SLOW_DOWN_FACTOR)
  
  def test_change_ghost_speed(self):
    Ghost.SLOW_DOWN_FACTOR = 1.7
    self.assertBasicGhostMovement(Ghost.SLOW_DOWN_FACTOR)

  def test_ghosts_only_change_direction_in_intersections(self):
    self.grid = PacManGrid(TEST_GRID_2)
    self.configure_pacman((0, 0), LEFT)
    self.ghost = self.grid.ghosts[0]
    self.ghost.direction = RIGHT
    self.advance_steps(2 * Ghost.SLOW_DOWN_FACTOR)
    self.assertClose(self.ghost.x, 5.5 * SQUARE_STEPS)
    self.advance_steps(3 * Ghost.SLOW_DOWN_FACTOR)
    self.assertClose(self.ghost.x, 2.5 * SQUARE_STEPS)

  def test_ghosts_optimal_paths_towards_pacman(self):
    self.grid = PacManGrid(TEST_GRID_3)
    self.upper_ghost = self.grid.ghosts[0]
    self.lower_ghost = self.grid.ghosts[1]

    self.configure_pacman((7, 0), DOWN)
    self.advance_steps(Ghost.SLOW_DOWN_FACTOR)
    self.assertGhostLocations((9, 4), (0, 3))
    self.advance_steps(Ghost.SLOW_DOWN_FACTOR)
    self.assertGhostLocations((9, 5), (0, 2))
    self.advance_steps(Ghost.SLOW_DOWN_FACTOR)
    self.assertGhostLocations((8, 5), (0, 3))


if __name__ == '__main__':
  unittest.main()