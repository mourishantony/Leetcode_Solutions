class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = Counter(arr)
        res = -1
        for key , value in ans.items():
            if key == value:
                res = max(res,key)
        return res