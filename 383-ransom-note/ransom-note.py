class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ans = {}

        for a in magazine:
            ans[a] = ans.get(a,0) + 1

        for a in ransomNote:
            if ans.get(a,0) == 0:
                return False
            ans[a]-=1
        return True