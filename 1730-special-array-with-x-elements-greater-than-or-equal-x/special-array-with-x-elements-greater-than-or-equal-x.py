class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        for x in range(1000):
            count = 0
            for num in nums:
                if num >= x:
                    count+=1
                if count > x:
                    break
            if count == x:
                return x
            if x>len(nums):
                return -1