class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        store ={}
        for i,val in enumerate(nums):
            if target - val in store:
                return [store[target- val],i]
            store[val] = i
