class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = {'a', 'e', 'i', 'o', 'u'}

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i]
            if words[i][0] in vowels and words[i][-1] in vowels:
                prefix[i + 1] += 1

        ans = []

        for l, r in queries:
            ans.append(prefix[r + 1] - prefix[l])

        return ans