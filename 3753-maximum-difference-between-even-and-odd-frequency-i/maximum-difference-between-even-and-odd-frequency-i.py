class Solution:
    def maxDifference(self, s: str) -> int:
        ans = Counter(s)
        mx = 0
        mn = float('inf')
        for i in ans.values():
            if i % 2 :
                mx = max(i,mx)
            else:
                mn = min(i,mn)
        return mx - mn