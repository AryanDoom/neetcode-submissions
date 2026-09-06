class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        p1=nums[0]
        p2=nums[0]
        while True:
            p1=nums[p1]
            p2=nums[nums[p2]]
            if p1==p2:
                break
        p1 = nums[0]
        while p1 != p2:
            p1 = nums[p1]
            p2 = nums[p2]
        return p1