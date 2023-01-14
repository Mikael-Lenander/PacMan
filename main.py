import pygame
import sys
from math import floor
from model import PacManGrid, PacMan
from constants import *

def draw(screen, grid, pacman, WIDTH, HEIGHT, SQUARE_SIZE):
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
      if square == ENEMY_PORT:
        pygame.draw.rect(screen, LIGHT_BROWN, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
      if (x, y) in grid.snacks:
        pygame.draw.circle(screen, YELLOW, (x * SQUARE_SIZE + SQUARE_SIZE // 2, y * SQUARE_SIZE + SQUARE_SIZE // 2), SQUARE_SIZE // 6)
  pygame.draw.circle(screen, (255, 0, 0), (floor(pacman.x / PacMan.SQUARE_STEPS * SQUARE_SIZE), floor(pacman.y / PacMan.SQUARE_STEPS * SQUARE_SIZE)), SQUARE_SIZE // 2)
          
  pygame.display.update()

def main():
  grid = PacManGrid(GRID)
  pacman = grid.pacman

  SQUARE_SIZE = 30
  WIDTH = grid.width * SQUARE_SIZE
  HEIGHT = grid.height * SQUARE_SIZE

  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
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

    clock.tick(pacman.SQUARE_STEPS * pacman.SQUARES_PER_SECOND)
    grid.update()
    draw(screen, grid, pacman, WIDTH, HEIGHT, SQUARE_SIZE)

if __name__ == "__main__":
    main()
