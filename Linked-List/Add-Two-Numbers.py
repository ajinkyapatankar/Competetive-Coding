# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1, node2 = l1,l2; carry = 0; ll = Linkedlist()
        while node1 or node2:
            val1 = 0 if not node1 else node1.val
            val2 = 0 if not node2 else node2.val
            sum = val1 + val2 + carry
            ll.append(ListNode(sum%10))
            carry = sum//10
            if node1: node1 = node1.next
            if node2: node2 = node2.next
        if carry>0:
            ll.append(ListNode(carry))
        return ll.head
            

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    def append(self,node):
        if self.head is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
    