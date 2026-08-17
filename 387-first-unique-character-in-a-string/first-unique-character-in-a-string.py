class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = Counter(s)
        for i in ans.keys():
            if ans[i] == 1:
                return s.index(i)
        return -1