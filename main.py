import numpy as np
# Ask for the size of the search area
meters = input("What is the squared footage of the area that we are searching? : ")
# convert from str type to int type
meters = int(meters)

# print a grid in the size defined by the user
grid =[]

for row in range(meters):
    grid.append([])
    for column in range(meters):
        grid[row].append('x')

# Value that the while loop with go unto
value = meters * meters

# Counter for while loop
counter = value;

# While loop for the Archimedean Spiral
#while counter > 0:
for row in range(1):
    grid.append([])
    for column in range(1):
        grid[row].append('0')

          #  counter -= 5

def print_grid(grid):
    for row in grid:
        print (" ".join(row))

# Print out the grid
print_grid(grid)