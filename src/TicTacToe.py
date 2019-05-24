import random

import numpy as np


def print_grid(grid):
    print("   " + grid[0, 0] + " | " + grid[0, 1] + " | " + grid[0, 2])
    print("  ---+---+---")
    print("   " + grid[1, 0] + " | " + grid[1, 1] + " | " + grid[1, 2])
    print("  ---+---+---")
    print("   " + grid[2, 0] + " | " + grid[2, 1] + " | " + grid[2, 2])
    print()


def check_centre_free(grid):
    return grid[1, 1] == " "


def check_row(row, piece):
    return list(row).count(piece)


def check_win(player):
    for row in grid:
        if check_row(row, player) == 3:
            return True
    for row in grid.transpose():
        if check_row(row, player) == 3:
            return True
    if check_row(grid.diagonal(), player) == 3 or check_row(np.fliplr(grid).diagonal(), player) == 3:
        return True
    return False


def computer_move(grid, player, opponent):
    if check_centre_free(grid):
        grid[1, 1] = player
        return

    oppsmax = [[-1, -1, -1, -1]]
    blockflag = False
    for j in range(3):
        for k in range(3):
            if grid[j, k] != " ":
                continue

            current_row = grid[j, :]
            current_col = grid[:, k]

            oppsrow = check_row(current_row, player)
            oppscol = check_row(current_col, player)

            blocksrow = check_row(current_row, opponent)
            blockscol = check_row(current_col, opponent)

            oppsdiag = 0
            blocksdiag = 0

            if j % 2 == 0 and k % 2 == 0:
                if j == k:
                    diag = grid.diagonal()
                else:
                    diag = np.fliplr(grid).diagonal()
                oppsdiag = check_row(diag, player)
                blocksdiag = check_row(diag, opponent)

            if oppsrow == 2 or oppscol == 2 or oppsdiag == 2:
                # win
                grid[j, k] = player
                return True

            if blocksrow == 2 or blockscol == 2 or blocksdiag == 2:
                # block
                blockflag = True
                blockwhere = [j, k]

            opps = (oppsdiag - blocksdiag) + (oppscol - blockscol) + (oppsrow - blocksrow)
            blocks = blocksdiag + blockscol + blocksrow

            # Rather than pick the first of equally weighted squares, it creates a list of squares of equal weight

            if opps > oppsmax[0][0] or (opps == oppsmax[0][0] and blocks > oppsmax[0][1]):
                oppsmax = [[opps, blocks, j, k]]
            elif opps == oppsmax[0][0] and blocks == oppsmax[0][1]:
                oppsmax.append([opps, blocks, j, k])
                print(oppsmax)
    if blockflag:
        grid[blockwhere[0], blockwhere[1]] = player
    else:
        rando = random.randint(0, len(oppsmax) - 1)
        grid[oppsmax[rando][2], oppsmax[rando][3]] = player
    return False


def human_move(player):
    move = int(input("Enter move (1-9)")) - 1
    x = move // 3
    y = move % 3
    while grid[x, y] != " ":
        move = int(input("Enter move (1-9)")) - 1
        x = move // 3
        y = move % 3
    grid[x, y] = human
    return check_win(player)


grid = np.full([3, 3], dtype=str, fill_value=" ")
computer, human = random.sample(["X", "O"], 2)
moves = (["X", "O"] * 5)[:9]
print()
print("You are playing {}. X always goes first.".format(human))
print()
print("Enter the number of a square to play there:")
print()
print_grid(np.arange(1, 10).reshape(3, 3).astype(str))
print()

for move in moves:
    if move == computer:
        win = computer_move(grid, computer, human)
    else:
        win = human_move(human)
    print_grid(grid)

    if win:
        if move == computer:
            print("Computer wins!")
        else:
            print("Player wins")
        break
if not win:
    print("It's a tie!")

"""    
check centre
    if free - take it (no other processing necessary for middle as it will always be occupied by end of move 2)
    
check square
    check row
    check col (grid.transpose row)
    if corner
        check diagonal (grid.diagonal.row)
    if win possible
        win
    else if must-block
        block
    else
        check squares with best opps
            if > 1 best opp
                block random best opp
            else
                block best opp
        
check row/col
    count blocks (opponent pieces in row)
    count opportunities (own pieces in row - opponent pieces in row)
        







        
"""
