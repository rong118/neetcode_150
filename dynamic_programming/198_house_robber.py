"""
198. House Robber (Medium)
https://leetcode.com/problems/house-robber/

You are a robber planning to rob houses along a street. Adjacent houses have security,
so you cannot rob two adjacent houses. Return the maximum amount you can rob.
"""
from typing import List


def rob(nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    prev2, prev1 = 0, 0
    for num in nums:
        prev2, prev1 = prev1, max(prev2 + num, prev1)

    return prev1
