"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        m = {None: None}
        copy = ListNode()
        curr, prev = head, copy
        while curr:
            prev.next = ListNode(curr.val)
            m[curr] = prev.next
            prev = prev.next
            curr = curr.next
        
        curr = head
        while curr:
            m[curr].random = m[curr.random]
            curr = curr.next

        return copy.next
