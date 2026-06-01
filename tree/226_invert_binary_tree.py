"""
226. Invert Binary Tree (Easy)
https://leetcode.com/problems/invert-binary-tree/

Given the root of a binary tree, invert the tree and return its root.
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
