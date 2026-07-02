class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set=set(nums)
        longest=0
        for i in nums_set:
            if i-1 not in nums_set:
                lenght=1
                while i+lenght in nums_set:
                    lenght=lenght+1
                longest=max(longest,lenght)
        return(longest)