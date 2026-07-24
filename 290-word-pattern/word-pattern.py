class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        word_to_pattern = {}
        pattern_to_word = {}

        for p,w in zip(pattern,words):
            if p in pattern_to_word:
                if pattern_to_word[p] != w:
                    return False
            else:
                pattern_to_word[p] = w

            if w in word_to_pattern:
                if word_to_pattern[w] != p:
                    return False
            else:
                word_to_pattern[w] = p

        return True