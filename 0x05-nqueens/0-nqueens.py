#!/usr/bin/python3
"""
The N queens puzzle is the challenge.
This program solves the N queens problem
"""
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)


board = [-1 for _ in range(n)]
column = set()
pos_diag = set()
neg_diag = set()

solutions = []


def is_safe(r, c):
    for prev_row in range(r):
        if board[prev_row] == c or \
           board[prev_row] - prev_row == c - r or \
           board[prev_row] + prev_row == c + r:
            return False
    return True


def solve_puzzle(row):
    if row == n:
        solutions.append(board[:])
        return

    for col in range(n):
        if is_safe(row, col):
            board[row] = col
            solve_puzzle(row + 1)
            board[row] = -1


solve_puzzle(0)

if solutions:
    for solution in solutions:
        formatted_solution = [[r, c] for r, c in enumerate(solution)]
        print(formatted_solution)