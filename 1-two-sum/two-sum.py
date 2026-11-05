class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        a = {}
        for i,num in enumerate(nums):
            b = target - num
            if b in a:
                return [a[b],i]
            a[num] = i
