class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        sec = 0
        T = tickets[k]
        for i,val in enumerate(tickets):
            if i<=k:
                if val < tickets[k]:
                    sec+=val
                else:
                    sec+=T
            else:
                if val < tickets[k]:
                    sec+=val  
                else:
                    sec+= T-1
        return sec