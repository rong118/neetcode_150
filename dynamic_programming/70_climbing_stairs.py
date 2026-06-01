"""
70. Climbing Stairs (Easy)
https://leetcode.com/problems/climbing-stairs/

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. How many distinct ways can you climb to the top?
"""
def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    one, two = 1, 2
    for _ in range(3, n + 1):
        one, two = two, one + two
    return two
