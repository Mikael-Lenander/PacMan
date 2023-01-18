SQUARE_STEPS = 40
SQUARES_PER_SECOND = 3
LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)
DIRECTIONS = (LEFT, RIGHT, UP, DOWN)
OPPOSITE_DIRECTION = { LEFT: RIGHT, RIGHT: LEFT, UP: DOWN, DOWN: UP }
CORNERS = ((-1, -1), (-1, 1), (1, -1), (1, 1))
WALL = 'X'
GHOST_PORT = 'P'
EMPTY = '.'
SNACK = '*'
GHOST = 'G'
GRID = [
  "************XX************",
  "*XXXX*XXXXX*XX*XXXXX*XXXX*",
  "*XXXX*XXXXX*XX*XXXXX*XXXX*",
  "*XXXX*XXXXX*XX*XXXXX*XXXX*",
  "**************************",
  "*XXXX*XX*XXXXXXXX*XX*X*XX*",
  "*XXXX*XX*XXXXXXXX*XX*X*XX*",
  "******XX****XX****XX******",
  "XXXXX*XXXXX*XX*XXXXX*XXXXX",
  "....X*XXXXX*XX*XXXXX*X....",
  "....X*XX**********XX*X....",
  "....X*XX*XXXPPXXX*XX*X....",
  "....X*XX*XG....GX*XX*X....",
  "....X****XG....GX****X....",
  "....X*XX*XG....GX*XX*X....",
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