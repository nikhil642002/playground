import itertools
from collections import Counter

import numpy as np


class Grid(object):
    newid = itertools.count()

    def __init__(self, grid):
        self.id = next(self.__class__.newid)
        self.grid = np.array(grid, dtype=object)
        self.unsolvable = False
        self.dupgrid = False  # True if this grid is only used for loop evaluation

    def __str__(self):
        return "Grid {}\n\n{}\n".format(self.id, self.grid)

    def solve_squares(self):
        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                square = self.grid[x:x + 3, y:y + 3]
                nums = set(filter(lambda x: isinstance(x, int), square.flatten()))
                for a in range(3):
                    for b in range(3):
                        if isinstance(self.grid[x + a, y + b], list):
                            # grid[x + a, y + b] = list(set(grid[x+a, y+b])- nums)
                            square[a, b] = list(set(square[a, b]) - nums)
                            vals = Counter(list(filter(lambda x: isinstance(x, int), square.flatten())))
                            if len(square[a, b]) == 0 or (
                                    len(vals) > 0 and vals[max(vals, key=lambda key: vals[key])] > 1):
                                self.unsolvable = True
                                return

                            if len(square[a, b]) == 1:
                                square[a, b] = int(square[a, b][0])

    def solve_rows(self):
        for row in self.grid:
            nums = set(filter(lambda x: isinstance(x, int), row))
            for ix, element in enumerate(row):
                if isinstance(element, list):
                    row[ix] = list(set(element) - nums)
                    vals = Counter(list(filter(lambda x: isinstance(x, int), row)))
                    if len(row[ix]) == 0 or (len(vals) > 0 and vals[max(vals, key=lambda key: vals[key])] > 1):
                        self.unsolvable = True
                        return
                    if len(row[ix]) == 1:
                        row[ix] = int(row[ix][0])

    def solve_columns(self):
        self.grid = self.grid.transpose()
        self.solve_rows()
        self.grid = self.grid.transpose()

    def copy(self):
        copyto = Grid([])
        copyto.grid = np.copy(self.grid)
        return copyto

    def dup(self, copyto):
        copyto.grid = np.copy(self.grid)
        copyto.dupgrid = True
        return copyto


    def solver(self):
        prev = Grid([])
        solved = False
        while not solved:
            if not self.unsolvable:
                self.solve_squares()
            if not self.unsolvable:
                self.solve_rows()
            if not self.unsolvable:
                self.solve_columns()
            if sum(filter(lambda x: isinstance(x, int), self.grid.flatten())) == 405:
                solved = True
                return solved
            if self.unsolvable:
                break
            if np.array_equal(self.grid, prev.grid):
                break
            prev = self.dup(prev)


    def new_solution_path(self):
        # current grid is unsolvable so need to try different solution paths
        # identify one of the unsolved squares with the shortest list of possibilities and create n new grids, each with
        #   that square set to one of the possible values and then attempt to re-solve each of those paths

        self.unsolvable = True  # mark current grid as a dead end
        open_lists = sorted(list(filter(lambda x: isinstance(x, list), self.grid.flatten())), key=lambda x: len(x))
        idx = list(self.grid.flatten()).index(open_lists[0])
        x, y = divmod(idx, 9)
        for i in range(len(open_lists[0])):
            grids.append(self.copy())  # create n new grids
            grids[-1].grid[x, y] = open_lists[0][i]  # set x, y in each grid to one of the possible values


def main(input):
    i = [a for a in range(1, 10)]
    for x in range(9):
        for y in range(9):
            if input[x][y] == 0:
                input[x][y] = i
    global grids
    grids = [Grid(input)]
    solved = grids[0].solver()
    if solved:
        return grids[0].grid.tolist()

    loop = 0
    while not solved:
        active = 0
        loop += 1
        for k in range(len(grids)):
            if not grids[k].unsolvable:
                active += 1
                grids[k].new_solution_path()
        # print("Loop {}, {} grids active".format(loop, active))

        for k in range(len(grids)):
            if not grids[k].unsolvable:
                solved = grids[k].solver()
                if solved:
                    return grids[k].grid.tolist()

        if loop > 100:
            print("There's probably an error in the starting grid")
            return None


if __name__ == '__main__':
    main(input)