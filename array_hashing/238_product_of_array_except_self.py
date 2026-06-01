"""
238. Product of Array Except Self (Medium)
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the
product of all the elements of nums except nums[i]. Must run in O(n) without division.
"""
from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [1] * n

    # Prefix products (left of i)
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    # Postfix products (right of i)
    postfix = 1
    for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]

    return res
