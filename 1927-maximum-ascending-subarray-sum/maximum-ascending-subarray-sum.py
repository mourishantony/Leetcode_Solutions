class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        inc = nums[0]
        ans = nums[0]

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                inc +=nums[i+1]
            else:
                inc = nums[i+1]
            ans = max(inc,ans)

        return ans
