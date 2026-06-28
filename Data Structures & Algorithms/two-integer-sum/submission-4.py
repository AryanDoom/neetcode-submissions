class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=dict()
        
        for indx , ele in enumerate(nums):
            needed= target - ele
            if needed in seen:
                return [seen[needed],indx]
            seen[ele] = indx
