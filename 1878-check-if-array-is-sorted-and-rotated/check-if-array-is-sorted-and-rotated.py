class Solution:
    def check(self, nums: List[int]) -> bool:
        list_rotates = [nums[i:] + nums[:i] for i in range(len(nums))]
        # print(list_rotates)
        for lists in list_rotates:
            if lists == sorted(nums):
                return True

        return False