class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        lst = [1]
        if rowIndex == 1:
            return [1,1]
        while rowIndex >0:
            lst[:] = [0] + lst + [0]
            i,j = 0,1
            temp = []
            while j<len(lst):
                temp.append(lst[i]+lst[j])
                i, j = j , j+1
            lst[:] = temp
            rowIndex-=1
        return lst