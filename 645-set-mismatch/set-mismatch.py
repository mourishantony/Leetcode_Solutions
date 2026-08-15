class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor = 0
        n = len(nums)

        for i in range(1, n + 1):
            xor ^= i

        for num in nums:
            xor ^= num

        bit = xor & -xor

        a = b = 0

        for i in range(1, n + 1):
            if i & bit:
                a ^= i
            else:
                b ^= i

        for num in nums:
            if num & bit:
                a ^= num
            else:
                b ^= num

        if a in nums:
            return [a, b]
        return [b, a]