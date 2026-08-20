class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # pos = customers[0][0] + customers[0][1]
        # sec = pos - customers[0][0]
        pos = 0
        sec =0
        for i,j in customers:
            if i < pos:
                pos += j
            else:
                pos = i + j
            sec += pos - i
        return sec/len(customers)