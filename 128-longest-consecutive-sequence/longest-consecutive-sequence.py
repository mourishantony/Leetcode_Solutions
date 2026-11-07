class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) < 1:
            return 0
        ans = 0
        temp = 1
        nums = list(set(nums))
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] -1 != nums[i-1]:
                ans = max(ans,temp)
                temp = 0
            temp+=1
        return max(ans,temp)