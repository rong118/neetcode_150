"""
98. Validate Binary Search Tree (Medium)
https://leetcode.com/problems/validate-binary-search-tree/

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isValidBST(root: Optional[TreeNode]) -> bool:
    def valid(node, left_bound, right_bound):
        if not node:
            return True
        if left_bound is not None and node.val <= left_bound:
            return False
        if right_bound is not None and node.val >= right_bound:
            return False
        return valid(node.left, left_bound, node.val) and valid(node.right, node.val, right_bound)

    return valid(root, None, None)
