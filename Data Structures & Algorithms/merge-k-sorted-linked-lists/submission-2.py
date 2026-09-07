# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(current1,current2):
            ans = ListNode()
            current = ans
            # current1 = list1
            # current2 = list2
            while current1 is not None and current2 is not None:
                if current1.val < current2.val:
                    current.next = current1
                    current1 = current1.next
                else:
                    current.next = current2
                    current2 = current2.next
                current = current.next
            if current1:
                current.next = current1
            else:
                current.next = current2
            return ans.next
        
        if not lists:
            return None
        
        while len(lists) > 1:
            merged_lists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merged_lists.append(merge(l1, l2))
            lists = merged_lists
        return lists[0]