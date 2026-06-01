"""
121. Best Time to Buy and Sell Stock (Easy)
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Given an array prices where prices[i] is the price of a given stock on the ith day,
maximize your profit by choosing a single day to buy and a different day in the future to sell.
Return the maximum profit, or 0 if no profit is possible.
"""
from typing import List


def maxProfit(prices: List[int]) -> int:
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            max_profit = max(max_profit, price - min_price)

    return max_profit
