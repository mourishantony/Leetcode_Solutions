class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        ans = Counter(s)
        flag = True
        count = 0
        for i in ans.keys():
            if ans[i] %2 != 0:
                count+=ans[i] - 1
                if flag:
                    count+=1
                    flag = False
            else:
                count += ans[i]

        return count