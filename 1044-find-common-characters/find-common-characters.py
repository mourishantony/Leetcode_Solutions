class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        a = words[0]
        ans = list(a)
        for i in a:
            for j in range(1,len(words)):
                if i not in words[j]:
                    ans.remove(i)
                    break
                else:
                    words[j] = words[j].replace(i,"",1)
        return ans