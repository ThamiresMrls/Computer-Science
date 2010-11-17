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
def make_grid():
    grid = []

    for l in range(6):
        row=[]
        for n in range(7):
            color = 9
            row.append(color)
        grid.append(row)
    # display the grid
    cell_size = 100
    run_display(grid, cell_size, on_click, 6)
def drop(col,p,grid,row):
    if grid[5][col]==9:
        grid[5][col]=p
    elif grid[4][col]==9:
        grid[4][col]=p
    elif grid[3][col]==9:
        grid[3][col]=p
    elif grid[2][col]==9:
        grid[2][col]=p
    elif grid[1][col]==9:
        grid[1][col]=p
    elif grid[0][col]==9:
        grid[0][col]=p
    #else:
    #    turn(p)
    return grid



def turn(row, col, grid, p):
    if col==0:
        drop(col,p,grid,row)
    elif col==1:
        drop(col,p,grid,row)
    elif col==2:
        drop(col,p,grid,row)
    elif col==3:
        drop(col,p,grid,row)
    elif col==4:
        drop(col,p,grid,row)
    elif col==5:
        drop(col,p,grid,row)
    elif col==6:
        drop(col,p,grid,row)
    else:
        print "Something's wrong"
    return grid


def on_click(grid, row, col, p):
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
    grid=turn(row, col, grid, p)
    print p
    return grid

make_grid()
