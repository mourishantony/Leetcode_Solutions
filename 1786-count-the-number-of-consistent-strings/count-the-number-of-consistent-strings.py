class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        for ch in allowed:
            for i in range(len(words)):
                 if ch in words[i]:
                    words[i] = words[i].replace(ch,"")
        count=0
        for word in words:
            if len(word)== 0:
                count+=1
        return count