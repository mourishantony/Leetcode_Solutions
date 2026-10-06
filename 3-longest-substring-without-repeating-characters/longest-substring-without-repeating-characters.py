class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        store = ""
        for a in s:
            if a in store:
                store = store[store.index(a)+1:]
            store +=a
            ans = max(len(store),ans)
        return ans