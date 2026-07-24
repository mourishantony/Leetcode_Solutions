class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowel_lst = [0] *n
        vowel = "aeiou"
        for i in range(n):
            if words[i][0] in vowel and words[i][-1] in vowel:
                vowel_lst[i] = 1
        #[1,0,1,1,1]

        count = [0] * n
        count[0] = vowel_lst[0]

        for i in range(1,len(vowel_lst)):
            count[i] = count[i-1] + vowel_lst[i]

        ans = []
        for i in range(len(queries)):
            l = queries[i][0]
            r = queries[i][-1]
            if l == 0:
                ans.append(count[r])
            else:
                ans.append(count[r] - count[l-1])

        return ans