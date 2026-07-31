class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        ans = Counter(nums)
        for key in ans.keys():
            if ans[key] %2 !=0:
                return False

        return True