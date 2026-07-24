class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = "balloon"
        counted = Counter(text)
        flag = "True"
        ans = {}
        for i in range(len(s)):
            if s[i] in counted:
                ans[s[i]] = counted[s[i]]
            else:
                return 0
        count = 0
        while flag:
            for i in s:
                if ans[i] > 0:
                    ans[i] -=1
                else:
                    return count
            count+=1
        
        return count