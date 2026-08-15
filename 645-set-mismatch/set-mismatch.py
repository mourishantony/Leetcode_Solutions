class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        l, r = 0, 0

        if nums[0] != 1:
            r = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                l = nums[i]
            elif nums[i] - 1 != nums[i - 1]:
                r = nums[i] - 1

            if l > 0 and r > 0:
                break

        if r == 0:
            r = len(nums)

        return [l, r]