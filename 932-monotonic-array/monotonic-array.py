class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        def inc(nums):
            high = -float(inf)
            for num in nums:
                if num <high:
                    return False
                high = num
            return True
        
        def dec(nums):
            low = float(inf)
            for num in nums:
                if num >low:
                    return False
                low = num
            return True
        
        return inc(nums) or dec(nums)