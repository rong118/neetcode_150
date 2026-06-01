"""
55. Jump Game (Medium)
https://leetcode.com/problems/jump-game/

You are given an integer array nums. You are initially positioned at the array's first index,
and each element represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""
from typing import List


def canJump(nums: List[int]) -> bool:
    goal = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0
