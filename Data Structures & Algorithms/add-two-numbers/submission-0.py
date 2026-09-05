# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) ->Optional[ListNode]:
        # len1=0
        # len2=0
        # curr1=l1
        # curr2=l2
        # while curr1!=None:
        #     len1=len1+1
        #     curr1=curr1.next
        # while curr2!=None:
        #     len2=len2+1
        #     curr2=curr2.next
        ans = ListNode(0)
        curr = ans
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10
            curr.next = ListNode(digit)
            curr = curr.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return ans.next