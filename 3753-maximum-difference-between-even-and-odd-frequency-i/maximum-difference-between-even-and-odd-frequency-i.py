class Solution:
    def maxDifference(self, s: str) -> int:
        ans = dict(Counter(s))
        odd =[]
        even = []
        for i in ans.keys():
            if ans[i] % 2 == 0:
                even.append(ans[i])
            else:
                odd.append(ans[i])
        return max(odd) - min(even)