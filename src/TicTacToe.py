import numpy as np


def print_grid(grid):
    print("----------")
    for row in grid:
        print(row[0] + "  | " + row[1] + " | " + row[2])
        print("----------")


def check_centre_free(grid):
    return grid[1, 1] == " "


def computer_move(grid, player, opponent):
    if check_centre_free(grid):
        grid[1, 1] = player
        return

    oppsmax = [-1, -1, -1]
    for j in range(3):
        for k in range(3):
            if grid[j, k] != " ":
                continue

            oppsrow = list(grid[j, :]).count(player)
            oppscol = list(grid[:, k]).count(player)

            blocksrow = list(grid[j, :]).count(opponent)
            blockscol = list(grid[:, k]).count(opponent)

            oppsdiag = 0
            blocksdiag = 0

            if j % 2 == 0 and k % 2 == 0:
                if j == k:
                    diag = [grid[0, 0], grid[1, 1], grid[2, 2]]
                else:
                    diag = [grid[0, 2], grid[1, 1], grid[2, 0]]
                oppsdiag = diag.count(player)
                blocksdiag = diag.count(opponent)

            if oppsrow == 2 or oppscol == 2 or oppsdiag == 2:
                # win
                grid[j, k] = player
                return True

            if blocksrow == 2 or blockscol == 2 or blocksdiag == 2:
                # block
                grid[j, k] = player
                return False

            opps = oppsdiag + oppscol + oppsrow
            blocks = blocksdiag + blockscol + blocksrow

            if opps > oppsmax[0] or (opps == oppsmax[0] and blocks > oppsmax[1]):
                oppsmax = [opps, blocks, j, k]
    grid[oppsmax[2], oppsmax[3]] = player
    return False


grid = np.full([3, 3], dtype=str, fill_value=" ")
computer_move(grid, "X", "O")
print_grid(grid)
for i in range(4):
    move = int(input("Enter move (1-9)")) - 1
    x = move // 3
    y = move % 3
    while grid[x, y] != " ":
        move = int(input("Enter move (1-9)")) - 1
    x = move // 3
    y = move % 3
    grid[x, y] = "O"
    print(x, y)
    print_grid(grid)
    computer_move(grid, "X", "O")
    print_grid(grid)

"""    
check centre
    if free - take it
    
check corners
    check side x 2
    check diagonal
        if win - win
        if opp-win
            block
        count blocks
        count opportunities
        
check middles
    check middle x 2
    if win - win
        if opp-win
            block
        count blocks
        count opportunities
        
make move
    check max opportunities
        check max blocks
            if > 1:
                random choice
    
123
456
789






        
"""
