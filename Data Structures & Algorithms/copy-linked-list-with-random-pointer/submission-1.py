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
        dih = {}
        curr = head
        while curr:
            dih[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            dih[curr].next = dih.get(curr.next)
            dih[curr].random = dih.get(curr.random)
            curr = curr.next
        return dih.get(head)