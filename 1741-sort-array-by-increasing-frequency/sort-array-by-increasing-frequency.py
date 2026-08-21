class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        store = Counter(nums)

        sorted_store = sorted(store.items(),key = lambda item : (item[1], -item[0]))
        ans = []
        for key,value in sorted_store:
            ans.extend([key] * value)
        return ans