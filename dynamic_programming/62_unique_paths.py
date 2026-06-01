"""
62. Unique Paths (Medium)
https://leetcode.com/problems/unique-paths/

A robot starts at the top-left corner of an m x n grid and can only move down or right.
Return the number of possible unique paths to the bottom-right corner.
"""
def uniquePaths(m: int, n: int) -> int:
    # Initialize bottom row (all 1s)
    row = [1] * n

    # For each row above the bottom, compute paths
    for _ in range(m - 1):
        new_row = [1] * n
        for col in range(1, n):
            new_row[col] = new_row[col - 1] + row[col]
        row = new_row

    return row[-1]
