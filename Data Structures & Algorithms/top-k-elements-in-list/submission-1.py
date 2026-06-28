import bisect
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen=set()
        nums.sort()
        ans=list()
        freqs=[]
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                continue
        #bisect.bisect_right(nums,element)
        for j in seen:
            freq=bisect.bisect_right(nums,j)-bisect.bisect_left(nums,j)
            freqs.append((freq, j))
            freqs.sort(reverse=True)

        for i in range(k):
            ans.append(freqs[i][1])

        return ans