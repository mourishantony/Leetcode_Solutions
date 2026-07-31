class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        ans = set()
        for num in nums:
            if num not in ans:
                ans.add(num)
            else:
                ans.remove(num)

        return len(ans) == 0