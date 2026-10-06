class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        store = []
        for a in range(len(s)):
            if s[a] in set(store):
                store = store[store.index(s[a])+1:]
            store.append(s[a])
            ans = max(len(store),ans)
        return ans