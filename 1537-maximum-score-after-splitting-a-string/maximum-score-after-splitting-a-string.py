class Solution:
    def maxScore(self, s: str) -> int:
        ans = 0
        for i in range(1,len(s)):
            l = s[:i].count("0")
            r = s[i:].count("1")
            ans = max(ans,l+r)
        return ans