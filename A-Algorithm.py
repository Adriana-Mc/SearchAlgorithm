import numpy as np

grid = [['x', 0, 'x'],
        [0, 'x', 0],
        [0, 0, 0]]

grid = np.array(grid)

def print_grid(grid):
    for row in grid:
        print (" ".join(row))

print_grid(grid)

