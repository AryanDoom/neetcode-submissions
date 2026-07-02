class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            if target-i in numbers:
                return([numbers.index(i)+1,numbers.index(target-i)+1])