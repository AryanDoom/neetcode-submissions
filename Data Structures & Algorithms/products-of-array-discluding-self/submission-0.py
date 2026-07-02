class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        if zero_count > 1:
            return [0] * len(nums)
        mul = 1
        for num in nums:
            if num != 0:
                mul *= num
        ans = []
        if zero_count == 1:
            for num in nums:
                if num == 0:
                    ans.append(mul)
                else:
                    ans.append(0)
        else:
            for num in nums:
                ans.append(mul // num)

        return ans