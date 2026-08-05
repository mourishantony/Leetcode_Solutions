class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        i=0
        s = {}
        for path in paths:
            s[path[0]] = path[1]

        ans = paths[0][0]
        while ans in s:
            ans = s[ans]
        return ans