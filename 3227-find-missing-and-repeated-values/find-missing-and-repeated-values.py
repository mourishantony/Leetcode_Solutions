class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        lst = [i for row in grid for i in row]
        ans = [0]*2
        temp = set()
        for i in range(len(lst)):
            if lst[i] not in temp:
                temp.add(lst[i])
            else:
                ans[0] = lst[i]
                break
        lst = set(lst)
        for i in range(1,len(lst)+2):
            if i not in lst:
                ans[1] = i

        return ans
            