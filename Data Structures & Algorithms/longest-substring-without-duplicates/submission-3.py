class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # seen=set()
        # ans=0
        # max_ans=0
        # if s == " ":
        #     return 1
        # for i in s:
        #     if i not in seen:
        #         seen.add(i)
        #         ans=ans+1
        #     else:
        #         max_ans=max(max_ans,ans)
        #         ans=0
        #         seen=set()
        #         seen.add(i)
        #         ans += 1
        # return max_ans
        seen = set()
        left = 0
        ans = 0
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            ans = max(ans, right - left + 1)
        return ans