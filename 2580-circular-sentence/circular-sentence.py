class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        s = sentence.split()
        if s[0][0] != s[-1][-1]:
            return False
        i=0 
        while i < len(s)-1:
            if s[i][-1] != s[i+1][0]:
                return False
            i+=1
        return True