#!/usr/bin/python3
""" Module for Prime Game """


def isWinner(x, nums):
    """Solves Prime Game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    flter = [True for _ in range(max(n + 1, 2))]
    for i in range(2, int(n**0.5) + 1):
        if not flter[i]:
            continue
        for j in range(i*i, n + 1, i):
            flter[j] = False

    flter[0] = flter[1] = False
    c = 0
    for i in range(len(flter)):
        if flter[i]:
            c += 1
        flter[i] = c

    winner_name = ''
    first_player = 0
    for n in nums:
        first_player += flter[n] % 2 == 1
    if first_player * 2 == len(nums):
        winner_name = None
    if first_player * 2 > len(nums):
        winner_name = "Maria"
    else:
        winner_name = "Ben"
    return winner_name