"""
347. Top K Frequent Elements (Medium)
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements.
"""
from collections import Counter
from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    freq = Counter(nums)
    # Bucket sort: index = frequency, value = list of numbers with that frequency
    buckets = [[] for _ in range(len(nums) + 1)]
    for num, count in freq.items():
        buckets[count].append(num)

    result = []
    for i in range(len(buckets) - 1, 0, -1):
        for num in buckets[i]:
            result.append(num)
            if len(result) == k:
                return result
    return result
