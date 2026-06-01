"""
153. Find Minimum in Rotated Sorted Array (Medium)
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Given a rotated sorted array of unique integers, return the minimum element. Must run in O(log n) time.
"""
from typing import List


def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2
        # If mid element is greater than rightmost, minimum is in the right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]
