LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)
OPPOSITE_DIRECTION = { LEFT: RIGHT, RIGHT: LEFT, UP: DOWN, DOWN: UP }
WALL = 'X'
ENEMY_PORT = 'P'
EMPTY = '.'
SNACK = '*'
GRID = [
  "************XX************",
  "*XXXX*XXXXX*XX*XXXXX*XXXX*",
  "*XXXX*XXXXX*XX*XXXXX*XXXX*",
  "*XXXX*XXXXX*XX*XXXXX*XXXX*",
  "**************************",
  "*XXXX*XX*XXXXXXXX*XX.X*XX*",
  "*XXXX*XX*XXXXXXXX*XX.X*XX*",
  "******XX****XX****XX******",
  "XXXXX*XXXXX*XX*XXXXX*XXXXX",
  "....X*XXXXX*XX*XXXXX*X....",
  "....X*XX**********XX*X....",
  "....X*XX*XXXPPXXX*XX*X....",
  "....X*XX*X......X*XX*X....",
  "....X****X......X****X....",
  "....X*XX*X......X*XX*X....",
  "....X*XX*XXXXXXXX*XX*X....",
  "....X*XX**********XX*X....",
  "....X*XX*XXXXXXXX*XX*X....",
  "XXXXX*XX*XXXXXXXX*XX*XXXXX",
  "******XX****XX****XX******",
  "*XXXX*XXXXX*XX*XXXXX*XXXX*",
  "*XXXX*XXXXX*XX*XXXXX*XXXX*",
  "***XX****************XX***",
  "XX*XX*XX*XXXXXXXX*XX*XX*XX",
  "XX*XX*XX*XXXXXXXX*XX*XX*XX",
  "******XX****XX****XX******",
  "*XXXXXXXXXX*XX*XXXXXXXXXX*",
  "*XXXXXXXXXX*XX*XXXXXXXXXX*",
  "**************************",
]