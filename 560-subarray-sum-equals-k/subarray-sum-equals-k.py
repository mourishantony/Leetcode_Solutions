class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum={0:1}
        sum = 0
        count =0
        for num in nums:
            sum+=num

            if sum - k in prefix_sum:
                count += prefix_sum[sum-k]
            prefix_sum[sum] = prefix_sum.get(sum,0) +1
        return count