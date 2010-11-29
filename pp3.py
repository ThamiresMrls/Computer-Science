##
## gol_getting_started.py
##
## by Kristina Striegnitz
##
## version 2/12/2010
##
## Code start from for an implementation of Conway's game of
## life. Fill in the missing code as described in the assignment.
##
from gol_display import run_game


ROWS = 50
COLS = 50
DEAD = 0
ALIFE = 1

def create_grid(rows, cols):
    """
    You need to complete this function.
    """
    grid = []
    for n in range(rows):
        row = []
        for i in range(cols):
            row.append(0)
        grid.append(row)
    return grid


def play_gol():

    grid = create_grid(ROWS, COLS)

    cell_size = 20
    run_game(grid, cell_size, on_click, next_gen)


def on_click(grid, row, col):
    """
    You need to complete this function.
    """
    if grid[row][col]==0:
        grid[row][col]=1
    else:
        grid[row][col]=0
    return grid

def life_neighbors(grid,row,col):
    """
    You need to complete this function.
    """
    n = 0
    for r in range(-1,2):
        for c in range(-1,2):
            if r==0 and c==0:
                pass
            elif grid[(row+r)%ROWS][(col+c)%COLS]==1:
                n+=1
    return n

def next_gen(grid):
    """
    You need to complete this function.
    """
    new_grid = create_grid(ROWS, COLS)
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c]==1:
                if life_neighbors(grid,r,c)<2:
                    new_grid[r][c]=0
                elif life_neighbors(grid,r,c)>3:
                    new_grid[r][c]=0
                else:
                    new_grid[r][c]=grid[r][c]
            else:
                if life_neighbors(grid,r,c)==3:
                    new_grid[r][c]=1
                else:
                    new_grid[r][c]=grid[r][c]
    return new_grid
play_gol()
