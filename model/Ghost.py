from constants import SQUARE_STEPS
import random
from math import floor
from .Character import Character

class Ghost(Character):
  SLOW_DOWN_FACTOR = 1.5
  BEST_DIRECTION_PROBABILITY = 0.7
  def __init__(self, grid, col, row):
    super().__init__(grid, col * SQUARE_STEPS + SQUARE_STEPS // 2, row * SQUARE_STEPS + SQUARE_STEPS // 2, (0, 0))
    self.steps_to_start = random.randint(0, 30) * SQUARE_STEPS

  def update(self):
    # if (self.grid.step_count < self.steps_to_start): 
      # return
    dx, dy = self.direction
    self.y += dy / self.SLOW_DOWN_FACTOR
    self.x += dx / self.SLOW_DOWN_FACTOR
    if self.grid.is_intersection(self.col(), self.row()) and self.grid.step_count % floor(SQUARE_STEPS * self.SLOW_DOWN_FACTOR) == 0:
      new_direction = self.best_direction_towards_pacman() if random.random() < self.BEST_DIRECTION_PROBABILITY else self.random_direction()
      # new_direction = self.best_direction_towards_pacman()
      self.direction = new_direction

  # Implemented with Dijkstra's algorithm
  def best_direction_towards_pacman(self):
    nodes = self.grid.nodes()
    source = (self.col(), self.row())
    target = self.grid.pacman.location
    dist = {}
    prev = {}
    visited = {}
    for node in nodes:
      dist[node] = float('inf')
      prev[node] = None
      visited[node] = False
    dist[source] = 0
    Q = nodes.copy()
    while len(Q) > 0:
      u = min(Q, key=lambda node: dist[node])
      visited[u] = True
      Q.remove(u)
      if u == target:
        break
      for v in [n for n in self.grid.neighbors(*u) if not visited[n]]:
        alt = dist[u] + 1
        if alt < dist[v]:
          dist[v] = alt
          prev[v] = u
    u = target
    while prev[u] is not None and prev[u] != source:
      u = prev[u]
    return u[0] - source[0], u[1] - source[1]
  
  def random_direction(self):
    return random.choice(self.grid.possible_directions(self.col(), self.row()))
    
