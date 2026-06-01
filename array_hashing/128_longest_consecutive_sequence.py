"""
128. Longest Consecutive Sequence (Medium)
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums, return the length of the longest consecutive
elements sequence. Must run in O(n) time.
"""
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    num_set = set(nums)
    ans = 0

    for num in nums:
        # Only start counting from the beginning of a sequence
        if num - 1 in num_set:
            continue

        length = 1
        while num + length in num_set:
            length += 1
        ans = max(ans, length)

    return ans
