class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        store ={}

        for i in range(len(nums)):
            if nums[i] in store and i- store[nums[i]] <= k:
                return True
            store[nums[i]] = i
        return False