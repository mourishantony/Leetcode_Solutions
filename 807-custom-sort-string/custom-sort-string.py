class Solution:
    def customSortString(self, order: str, s: str) -> str:
        ans = ""
        for o in order:
            if o in s:
                ans+=o*s.count(o)
                s = s.replace(o,"")
        return ans+s