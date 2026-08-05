class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        i=0
        s = {}
        for path in paths:
            s[path[0]] = path[1]

        p = []
        for path in paths:
            p.append(path[0])

        flag = True
        ans = paths[0][0]
        while flag:
            if ans in p:
                ans = s[ans]
            else:
                flag = False

        return ans