class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,1000):
            add =1
            sol=i
            while i>0:
                temp = i%10
                add*=temp
                i= i//10
            if add %t==0:
                return sol 