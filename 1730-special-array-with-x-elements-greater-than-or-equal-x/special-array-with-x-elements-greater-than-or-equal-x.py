class Solution:
    def specialArray(self, nums: List[int]) -> int:
        i=len(nums)
        while(i>0):
            count = 0
            for num in nums:
                if num >= i:
                    count+=1
            if i == count:
                return count
            i-=1
        return -1
