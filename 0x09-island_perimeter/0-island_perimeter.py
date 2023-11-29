#!/usr/bin/python3
"""
This script resolves the island perimeter.
"""


def island_perimeter(grid):
    """This function returns the perimeter of the island"""
    x = len(grid)
    y = len(grid[0])

    answer = 0
    for i in range(x):
        for j in range(y):
            if grid[i][j] == 1:
                cur = 4
                # right-horizontal neighbor exist
                if i + 1 < x and grid[i + 1][j] == 1:
                    cur -= 1
                # left - horizontal neighbor exist
                if i - 1 >= 0 and grid[i - 1][j] == 1:
                    cur -= 1
                # top neighbor exist
                if j + 1 < y and grid[i][j + 1] == 1:
                    cur -= 1
                # bottom neighbor exist
                if j - 1 >= 0 and grid[i][j - 1] == 1:
                    cur -= 1
                answer += cur
    return answer