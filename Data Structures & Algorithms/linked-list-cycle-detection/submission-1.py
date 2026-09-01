# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current1=head
        current2=head
        while current1 != None and current2 != None and current2.next!=None:
            current1=current1.next
            current2=current2.next.next
            if current1==current2:
                return True
        return False


        