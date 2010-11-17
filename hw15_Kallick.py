##
## example_grid.py
##
## by Kristina Striegnitz
##
## version 2/10/2010
##
## Demonstrates how the functions in file grid_display can be used.
##
## Additions to make cool game work by Daniel Dyssegaard Kallick
import random
from grid_display import run_display
DIMENSIONS=5
def make_grid(DIMENSIONS):
    grid = []

    for l in range(DIMENSIONS):
        row=[]
        for n in range(DIMENSIONS):
            color = random.choice([4,7])
            row.append(color)
        grid.append(row)
    # display the grid
    cell_size = 100
    run_display(grid, cell_size, on_click)


def toggle(color):
    if color==7:
        color=4
    else:
        color=7
    return color
def change_outside(row, col, grid):
    global DIMENSIONS
    grid[row][col]=toggle(grid[row][col])
    if row+1<=DIMENSIONS-1:
        grid[row+1][col]=toggle(grid[row+1][col])
    if row-1>=0:
        grid[row-1][col]=toggle(grid[row-1][col])
    if col+1<=DIMENSIONS-1:
        grid[row][col+1]=toggle(grid[row][col+1])
    if col-1>=0:
        grid[row][col-1]=toggle(grid[row][col-1])
    return grid
def on_click(grid, row, col):
    """
    This function specifies what should happen when there was a mouse
    click somewhere on the grid. The function gets called from the
    display, whenever a mouse click is registered. When it is called,
    the grid representation and two numbers indicating which row and
    column the mouse click was in are passed as parameter values. This
    function has to return the grid representation (potentially after
    modifying it).

    For the purposes of this example, we are not doing anything
    interesting when the grid gets clicked, we are just printing out
    which row and column the click was in.
    """
   # print row, col
    grid=change_outside(row, col, grid)

    return grid

make_grid(DIMENSIONS)
