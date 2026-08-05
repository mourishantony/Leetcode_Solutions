class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(num) <= magazine.count(num) for num in ransomNote)