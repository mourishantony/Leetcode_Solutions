class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            flag =  True
            for ch in word:
                if word.count(ch) > chars.count(ch):
                    flag = False
                    break
            if flag:
                count += len(word)
            
        return count