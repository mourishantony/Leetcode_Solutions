class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        store = [0] *26
        for word in words:
            for ch in word:
                store[ord(ch) -97]  +=1
        
        return all(i % len(words) == 0 for i in store)