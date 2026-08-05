class Solution:
    def largestGoodInteger(self, num: str) -> str:
        a,b,c = 0,1,2
        ans =0
        flag =  False
        while c < len(num):
            if num[a] == num[b] and num[a] == num[c]:
                flag = True
                ans = max(ans,int(num[a]))
            a,b,c = b,c,c+1
        return str(ans)*3 if flag else ""