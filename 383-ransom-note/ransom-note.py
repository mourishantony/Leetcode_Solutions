class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        ans = {}

        for a in ransomNote:
            ans[a] = ans.get(a,0) + 1

        for a in ans.keys():
            if magazine.count(a) < ans[a]:
                return False
        return True