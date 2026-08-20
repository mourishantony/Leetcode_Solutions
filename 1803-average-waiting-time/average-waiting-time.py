class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        pos = customers[0][0] + customers[0][1]
        sec = pos - customers[0][0]
        for i in range(1,len(customers)):
            if customers[i][0] < pos:
                pos += customers[i][1]
            else:
                pos = customers[i][0] + customers[i][1]
            sec += pos - customers[i][0] 
        return sec/len(customers)