class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,1000):
            add =1
            sol=i
            while sol>0:
                temp = sol%10
                add*=temp
                sol= sol//10
            if add %t==0:
                return i 