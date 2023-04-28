#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./0-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
#!/usr/bin/python3
import sys

def nQueens(N):
    def isSafe(row, col, slashCode, backslashCode,
            rowLookup, slashCodeLookup, backslashCodeLookup):
        if (slashCodeLookup[slashCode[row][col]] or
                backslashCodeLookup[backslashCode[row][col]] or
                rowLookup[row]):
            return False
        return True

    def printSolution(board):
        res = []
        for i in range(N):
            row = []
            for j in range(N):
                if board[i][j] == 1:
                    row.append([i, j])
            res.append(row)
        return res

    def solveNQueensUtil(
            board, col, slashCode, backslashCode, 
            rowLookup, slashCodeLookup, backslashCodeLookup, solutions):
        if col >= N:
            solutions.append(printSolution(board))
            return True
        res = False
        for i in range(N):
            if isSafe(i, col, slashCode, backslashCode,
                    rowLookup, slashCodeLookup, backslashCodeLookup):
                board[i][col] = 1
                rowLookup[i] = True
                slashCodeLookup[slashCode[i][col]] = True
                backslashCodeLookup[backslashCode[i][col]] = True
                res = solveNQueensUtil(
                    board, col + 1, slashCode, backslashCode,
                    rowLookup, slashCodeLookup, backslashCodeLookup, solutions) or res
                board[i][col] = 0
                rowLookup[i] = False
                slashCodeLookup[slashCode[i][col]] = False
                backslashCodeLookup[backslashCode[i][col]] = False
        return res

    if not isinstance(N, int):
        print("N must be a number")
        exit(1)

    if N < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0 for x in range(N)]for y in range(N)]
    # helper matrices
    slashCode = [[0 for x in range(N)]for y in range(N)]
    backslashCode = [[0 for x in range(N)]for y in range(N)]

    rowLookup = [False] * N

    x = 2 * N - 1
    slashCodeLookup = [False] * x
    backslashCodeLookup = [False] * x

    for rr in range(N):
        for cc in range(N):
            slashCode[rr][cc] = rr + cc
            backslashCode[rr][cc] = rr - cc + 7

    solutions = []
    if solveNQueensUtil(
            board, 0, slashCode, backslashCode, 
            rowLookup, slashCodeLookup, backslashCodeLookup, solutions) is False:
        return []

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        N = int(sys.argv[1])
    except:
        print("N must be a number")
        exit(1)
    solutions = nQueens(N)
    for solution in solutions:
        print(solution)
