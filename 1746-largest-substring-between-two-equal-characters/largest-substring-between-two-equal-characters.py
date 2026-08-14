class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        a = Counter(s)
        ans = 0
        flag = False
        for i in range(len(s)):
            if a[s[i]] > 1:
                for j in range(len(s)-1,-1,-1):
                    if s[i] == s[j]:
                        ans = max(ans,j-i-1)
                        flag = True 
        return ans if flag else -1