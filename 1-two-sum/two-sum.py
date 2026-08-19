class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(1,len(nums)):
            for j in range(i,len(nums)):

                if nums[j] + nums[j-i] == target:
                    return [j-i,j]