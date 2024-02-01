#!/usr/bin/python3
"""
This script determines the fewest number of coins
needed to meet a given total
"""


def makeChange(coins, total):
    """
    Args:
    coins ([list]): a list of the values of the coins in your possession
    total ([number]): amount
    Return: fewest number of coins needed to meet total
    """
    if total <= 0:
        return 0

    sorted_coins = sorted(coins, reverse=True)
    count = 0

    for i in sorted_coins:
        if (i > 0) and (i <= total):
            quotient = total // i
            count += quotient
            total -= quotient * i

    return count if total == 0 else -1