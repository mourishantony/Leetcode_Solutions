class Solution:
    def minOperations(self, s: str) -> int:
        compare1 = "01"*(int(len(s)//2)+1)
        compare2 = "10"*(int(len(s)//2)+1)
        count1 = 0
        count2 = 0
        for i in range(len(s)):
            if compare1[i] != s[i]:
                count1+=1
            if compare2[i] != s[i]:
                count2+=1
        return min(count1,count2)  