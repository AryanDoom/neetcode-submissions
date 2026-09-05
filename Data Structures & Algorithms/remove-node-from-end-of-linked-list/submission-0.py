# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr=head
        leng=0
        while curr != None:
            leng=leng+1
            curr=curr.next
        want=leng-n+1
        want_before=want-1
        if want_before==0:
            return head.next
        curr=head
        for k in range(want_before-1):
            curr=curr.next
        curr.next=curr.next.next
        return head


        