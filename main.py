import pygame
from pygame import gfxdraw
import sys
from math import floor, pi, sin
from model import PacManGrid
from constants import *

def pacman_mouth_angles(direction, step_count):
  angle_centers = { LEFT: pi, RIGHT: 0, UP: pi / 2, DOWN: 3 * pi / 2 }
  angle_center = angle_centers[direction]
  angle_range = pi / 6
  angle_offset = angle_range * abs(sin(step_count / SQUARE_STEPS * pi))
  return angle_center + angle_offset, angle_center - angle_offset

def draw(screen, grid, pacman, IMAGES, WIDTH, HEIGHT, SQUARE_SIZE):
  BLUE = (0, 0, 255)
  YELLOW = (255, 255, 0)
  BLACK = (0, 0, 0)
  LIGHT_BROWN = (255, 175, 164)
  WALL_THICKNESS = 5

  screen.fill(BLACK)
  pygame.draw.lines(screen, BLUE, True, [(0, 0), (WIDTH, 0), (WIDTH, HEIGHT), (0, HEIGHT)], WALL_THICKNESS)
  for y in range(grid.height):
    for x in range(grid.width):
      square = grid.grid[y][x]
      if square == WALL:
        pygame.draw.rect(screen, BLUE, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), WALL_THICKNESS)
      if square == GHOST_PORT:
        pygame.draw.rect(screen, LIGHT_BROWN, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
      if (x, y) in grid.snacks:
        pygame.draw.circle(screen, YELLOW, (x * SQUARE_SIZE + SQUARE_SIZE // 2, y * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 6)

  start_angle, end_angle = pacman_mouth_angles(pacman.direction, grid.step_count)
  pygame.draw.arc(screen, YELLOW, (floor((pacman.x / SQUARE_STEPS - 1/2) * SQUARE_SIZE), floor((pacman.y / SQUARE_STEPS - 1/2) * SQUARE_SIZE), SQUARE_SIZE - 1, SQUARE_SIZE - 1), start_angle, end_angle, SQUARE_SIZE // 2)
  
  for ghost in grid.ghosts:
    screen.blit(IMAGES[GHOST], (floor((ghost.x / SQUARE_STEPS - 1/2) * SQUARE_SIZE), floor((ghost.y / SQUARE_STEPS - 1/2) * SQUARE_SIZE)))

  pygame.display.update()

def main():
  grid = PacManGrid(GRID)
  pacman = grid.pacman

  SQUARE_SIZE = 30
  WIDTH = grid.width * SQUARE_SIZE
  HEIGHT = grid.height * SQUARE_SIZE
  GHOST_IMG = pygame.transform.scale(pygame.image.load('images/ghost.png'), (SQUARE_SIZE, SQUARE_SIZE))
  IMAGES = { GHOST: GHOST_IMG }

  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption('PacMan')
  clock = pygame.time.Clock()

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        sys.exit()
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          pacman.change_direction(LEFT)
        if event.key == pygame.K_RIGHT:
          pacman.change_direction(RIGHT)
        if event.key == pygame.K_UP:
          pacman.change_direction(UP)
        if event.key == pygame.K_DOWN:
          pacman.change_direction(DOWN)

    clock.tick(SQUARE_STEPS * SQUARES_PER_SECOND)
    grid.update()
    draw(screen, grid, pacman, IMAGES, WIDTH, HEIGHT, SQUARE_SIZE)

if __name__ == "__main__":
    main()