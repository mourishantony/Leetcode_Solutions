class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        count = [0] *n
        vowel = "aeiou"
        count[0] = 1 if words[0][0] in vowel and words[0][-1] in vowel else 0
        for i in range(1,n):
            if words[i][0] in vowel and words[i][-1] in vowel:
                count[i] = 1 + count[i-1]
            else:
                count[i] = count[i-1]
        #[1,0,1,1,1]
        ans = []
        for i in range(len(queries)):
            l = queries[i][0]
            r = queries[i][-1]
            if l == 0:
                ans.append(count[r])
            else:
                ans.append(count[r] - count[l-1])

        return ans