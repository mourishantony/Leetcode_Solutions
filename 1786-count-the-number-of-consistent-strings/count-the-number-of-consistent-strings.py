class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        temp = 0
        for word in words:
            for ch in word:
                if ch not in allowed:
                    temp +=1
                    break

        return len(words) - temp