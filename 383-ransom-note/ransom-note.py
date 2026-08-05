class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for num in ransomNote:
            if ransomNote.count(num) > magazine.count(num):
                return False
        return True 