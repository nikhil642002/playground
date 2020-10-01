# playground
Promote Python for Better Exeperience
Repo for small, standalone coding ideas

## Suduko Solver
Sudoku solver was one of the ideas that came up at a recent London Python Coder Dojo. As it was downvoted, I decided to have a crack at one myself.

The principle I adopted is of resolving the grid either to knowns or lists of possible values. If not resolved on the first pass, it then chooses one square with the lowest number of possible values and creates grids with each possibility filled in for that square and then attempts to solve all three. Any that are obviously invalid are eliminated. For any that are potentially valid but still can't be solved, the process is iterated by choosing another square and repeating the process.
