import pygame
import sys
from math import floor, pi, sin
from time import sleep
import tkinter as tk
from tkinter import messagebox
from model import Game
from constants import *

def pacman_mouth_angles(direction, step_count):
  angle_centers = { LEFT: pi, RIGHT: 0, UP: pi / 2, DOWN: 3 * pi / 2 }
  angle_center = angle_centers[direction]
  angle_range = pi / 6
  angle_offset = angle_range * abs(sin(step_count / SQUARE_STEPS * pi))
  return angle_center + angle_offset, angle_center - angle_offset

def draw(screen, grid, pacman, lives, IMAGES, WIDTH, HEIGHT, SQUARE_SIZE, STATUS_BAR_HEIGHT):
  BLUE = (0, 0, 255)
  YELLOW = (255, 255, 0)
  BLACK = (0, 0, 0)
  LIGHT_BROWN = (255, 175, 164)
  WALL_THICKNESS = 5

  screen.fill(BLACK)
  pygame.draw.lines(screen, BLUE, True, [(0, 0), (WIDTH, 0), (WIDTH, HEIGHT - STATUS_BAR_HEIGHT), (0, HEIGHT - STATUS_BAR_HEIGHT)], WALL_THICKNESS)
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

  for i in range(lives):
    m = 5
    pygame.draw.arc(screen, YELLOW, (WIDTH - (i + 1) * STATUS_BAR_HEIGHT, HEIGHT - STATUS_BAR_HEIGHT + m, STATUS_BAR_HEIGHT - 2*m, STATUS_BAR_HEIGHT - 2*m), pi / 6, 11 * pi / 6, STATUS_BAR_HEIGHT // 2)

  pygame.display.update()


def alert(game_lost):
  root = tk.Tk()
  root.withdraw()
  result = ''
  if game_lost:
    result = messagebox.askquestion('PacMan', 'Game over! Do you want to play again?')
  else:
    result = messagebox.askquestion('PacMan', 'You win! Do you want to play again?')
  root.destroy()
  return result

def main():
  game = Game()

  SQUARE_SIZE = 30
  STATUS_BAR_HEIGHT = 40
  WIDTH = game.grid.width * SQUARE_SIZE
  HEIGHT = game.grid.height * SQUARE_SIZE + STATUS_BAR_HEIGHT
  GHOST_IMG = pygame.transform.scale(pygame.image.load('images/ghost.png'), (SQUARE_SIZE, SQUARE_SIZE))
  IMAGES = { GHOST: GHOST_IMG }

  pygame.init()
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  pygame.display.set_caption('PacMan')
  clock = pygame.time.Clock()

  while True:
    grid = game.grid
    pacman = grid.pacman

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
    draw(screen, grid, pacman, game.lives, IMAGES, WIDTH, HEIGHT, SQUARE_SIZE, STATUS_BAR_HEIGHT)
    grid.update()

    if game.is_intercepted(SQUARE_SIZE / 2):
      if game.is_over():
        new_game = alert(game.is_lost())
        if new_game == 'yes':
          game = Game()
        else:
          sys.exit()
      else:
        sleep(0.8)
        game.resume()

if __name__ == "__main__":
    main()