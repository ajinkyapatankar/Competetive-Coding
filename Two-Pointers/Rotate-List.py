# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n, pre, current = 0, None, head
        while current:
            pre, current = current, current.next
            n += 1

        if not n or not k % n:
            return head

        tail = head
        for _ in range(n - k % n - 1):
            tail = tail.next

        next, tail.next, pre.next = tail.next, None, head
        return next