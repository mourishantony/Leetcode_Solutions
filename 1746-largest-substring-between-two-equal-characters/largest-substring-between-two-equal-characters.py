class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ans = -1
        store = {}
        for i in range(len(s)):
            if s[i] in store:
                ans = max(ans,i - store[s[i]] -1)
            else:
                store[s[i]] = i
        return ans