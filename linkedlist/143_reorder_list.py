"""
141. Linked List Cycle (Easy)
https://leetcode.com/problems/linked-list-cycle/

Given head of a linked list, determine if the linked list has a cycle in it.
Return true if there is a cycle, false otherwise.

Note: The Go file is named 143_reorder_list.go but actually implements hasCycle (problem 141).
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def hasCycle(head: Optional[ListNode]) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
