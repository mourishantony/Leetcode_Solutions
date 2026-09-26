class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        ans = len(nums) *[0]
        if len(nums) < 2:
            return nums
        
        for i in range(len(nums)):
            index = i + nums[i]
            if abs(index) >= len(nums):
                index %=len(nums)
            ans[i] = nums[index]
        return ans