class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        store = {}
        for word in words:
            for ch in word:
                store[ch]  = store.get(ch,0)+1
        
        for i in store.keys():
            if store[i] % len(words) !=0:
                return False
        return True