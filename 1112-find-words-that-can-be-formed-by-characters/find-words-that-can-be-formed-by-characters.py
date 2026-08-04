class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        for word in words:
            temp = chars
            count +=len(word)
            for char in word:
                if char in temp:
                    temp = temp.replace(char,"",1)
                else:
                    count -=len(word)
                    break
            
        return count