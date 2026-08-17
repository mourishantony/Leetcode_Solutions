class Solution:
    def firstUniqChar(self, s: str) -> int:
        ans = Counter(s)
        for i,ch in enumerate(s):
            if ans[ch] == 1:
                return i
        return -1