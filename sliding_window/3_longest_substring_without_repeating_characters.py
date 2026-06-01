"""
3. Longest Substring Without Repeating Characters (Medium)
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.
"""
def lengthOfLongestSubstring(s: str) -> int:
    char_index = {}
    left = 0
    ans = 0

    for right, ch in enumerate(s):
        if ch in char_index and char_index[ch] >= left:
            left = char_index[ch] + 1
        char_index[ch] = right
        ans = max(ans, right - left + 1)

    return ans
