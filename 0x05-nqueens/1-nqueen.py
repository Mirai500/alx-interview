import sys

if len(sys.argv) != 2:
	print('Usage: nqueens N')
	sys.exit(1)

try:
    n = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    sys.exit(1)

if n < 4:
	print('N must be greater than 4')
	sys.exit(1)
    

board = [['0' for _ in range(n)] for _ in range(n)]
column = set()
pos_diag = set()
neg_diag = set()

solutions = []

def is_safe(r, c):
    if c in column or (r + c) in pos_diag or (r - c) in neg_diag:
        return False
    return True

def solve_puzzle(r):
    if r == n:
        board_row = [' '.join(col) for col in board]
        solutions.append(board_row)
        return
        
    for c in range(n):
        if is_safe(r, c):
            column.add(c)
            pos_diag.add(r + c)
            neg_diag.add(r - c)
            board[r][c] = '1'
            solve_puzzle(r + 1)
            column.remove(c)
            pos_diag.remove(r + c)
            neg_diag.remove(r - c)
            board[r][c] = '0'
        
solve_puzzle(0)

if solutions:
    for i in solutions:
        for j in i:
            print(j)
        print()