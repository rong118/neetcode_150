"""
20. Valid Parentheses (Easy)
https://leetcode.com/problems/valid-parentheses/

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
"""
def isValid(s: str) -> bool:
    pairs = {')': '(', '}': '{', ']': '['}
    stack = []

    for ch in s:
        if ch in pairs.values():
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0
