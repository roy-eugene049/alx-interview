#!/usr/bin/python3
"""Calculate the fewest number of operations needed to get n H's in a file"""
def minOperations(n):
    """
    Calculate the fewest number of operations needed to get n H's in a file.

    Args:
        n (int): The number of H's to achieve.

    Returns:
        int: The fewest number of operations needed to get n H's, or 0 if impossible.
    """
    if n < 1:
        return 0  # impossible to achieve
    num_h = 1  # start with one H
    ops = 0  # number of operations performed
    clipboard = 0  # number of H characters in clipboard
    while num_h < n:
        if clipboard > 0:
            # if there are H characters in clipboard, paste them
            num_h += clipboard
            clipboard = 0
            ops += 1
        else:
            # if clipboard is empty, copy all H characters
            clipboard = num_h
            ops += 1
        if num_h == n:
            # if desired number of H characters is reached, return number of operations
            return ops
    return 0  # impossible to achieve
