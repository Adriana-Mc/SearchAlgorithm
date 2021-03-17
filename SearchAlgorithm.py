import numpy as np

# Ask for the size of the search area
meters = input("What is the squared footage of the area that we are searching? : ")
# convert from str type to int type
meters = int(meters)

# print a grid in the size defined by the user
grid =[]

# x's populate the unsearched area
for row in range(meters):
    grid.append([])
    for column in range(meters):
        grid[row].append('x')

# Print out the grid to the console
def print_grid(grid):
    for row in grid:
        print (" ".join(row))

# Print out the grid
print_grid(grid)

# Value that the while loop will go unto
value = meters * meters

grid = np.array(grid)
counter = 0

# Grid x and y values
x = 0
y = 0

def one(x, y, counter):
    if y < meters + 1:
        grid[x, y] = 0
        y += 1
        print(x, y)
        counter += 1
        return x
        return y
        return counter

# Archimedean can fuck this spiral for all I care
while counter < value:
    grid[x, y] = 0
    y += 1
    if y == meters:
        y = y - 1
        grid[x, y] = 0
        x += 1
        if x == meters:
            x = x - 1
            while y != -1:
                y -= 1
                grid[x, y] = 0
            y = y + 1
            while x > 0:
                x -= 1
                grid[x, y] = 0
            x = x + 1
            while y < (meters - 1):
                y += 1
                grid[x, y] = 0
            y = y - 1
            while x < (meters - 1):
                x += 1
                grid[x, y] = 0
            x = x - 1
            while y > (0 + 1):
                y -= 1
                grid[x, y] = 0
            while x > (0 + 1):
                x -= 1
                grid[x, y] = 0
                print(x, y)
                print(counter)
            break

    counter += 1


print_grid(grid)