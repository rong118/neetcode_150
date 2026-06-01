"""
11. Container With Most Water (Medium)
https://leetcode.com/problems/container-with-most-water/

Given an integer array height of length n, find two lines that together with the x-axis
form a container that holds the most water. Return the maximum amount of water a container can store.
"""
from typing import List


def maxArea(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    ans = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        ans = max(ans, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return ans
