"""
19. Remove Nth Node From End of List (Medium)
https://leetcode.com/problems/remove-nth-node-from-end-of-list/

Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    fast = slow = dummy

    # Advance fast by n steps
    for _ in range(n):
        fast = fast.next

    # Move both until fast reaches the end
    while fast.next:
        slow = slow.next
        fast = fast.next

    # Remove the nth node
    slow.next = slow.next.next
    return dummy.next
