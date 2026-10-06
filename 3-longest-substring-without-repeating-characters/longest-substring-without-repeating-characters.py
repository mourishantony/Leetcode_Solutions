class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        store = ""
        for a in range(len(s)):
            while s[a] in store:
                store = store[1:]
            store+=s[a]
            ans = max(len(store),ans)
        return ans