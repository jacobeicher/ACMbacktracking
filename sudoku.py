import numpy as np
from numpy.lib.type_check import iscomplex

def legal(puzzle, col, row, num):
    for i in range(0,9):
        if puzzle[col][i] == num:
            return False
        if puzzle[i][row] == num:
            return False

    xstart = (row//3)*3
    ystart = (col//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if puzzle[ystart + i][xstart + j] == num:
                return False
    
    return True



def solve(puzzle):
    for x in range(9):
        for y in range(9):
            if puzzle[y][x] == 0:
                for n in range(1, 10):
                    if legal(puzzle, y, x, n):
                        puzzle[y][x] = n
                        solve(puzzle)
                        puzzle[y][x] = 0
                return
    print(np.matrix(puzzle))
    return



def main():
    puzzle= [[5, 3, 0, 0, 7, 0, 0, 0, 0], 
            [6, 0, 0, 1, 9, 5, 0, 0, 0], 
            [0, 9, 8, 0, 0, 0, 0, 6, 0], 
            [8, 0, 0, 0, 6, 0, 0, 0, 3], 
            [4, 0, 0, 8, 0, 3, 0, 0, 1], 
            [7, 0, 0, 0, 2, 0, 0, 0, 6], 
            [0, 6, 0, 0, 0, 0, 2, 8, 0], 
            [0, 0, 0, 4, 1, 9, 0, 0, 5], 
            [0, 0, 0, 0, 8, 0, 0, 7, 9]]

    solve(puzzle)
if __name__ == "__main__":
    main()
