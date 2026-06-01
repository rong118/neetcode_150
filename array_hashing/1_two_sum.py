"""
1. Two Sum (Easy)
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target. You may assume exactly one solution exists.
"""
from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    m = {}
    for idx, num in enumerate(nums):
        diff = target - num
        if diff in m:
            return [m[diff], idx]
        m[num] = idx
    return []
