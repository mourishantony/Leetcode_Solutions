class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) ==1:
            return nums
        store = Counter(nums)
        sorted_store = {k:v for k,v in islice(sorted(store.items(),key = lambda item : item[1],reverse = True),k)}
        ans = list(sorted_store.keys())
        return ans