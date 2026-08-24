class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) ==1:
            return nums
        store = Counter(nums)
        sorted_store = {k:v for k,v in sorted(store.items(),key = lambda item : item[1],reverse = True)}
        # print(sorted_store)
        ans = list(sorted_store.keys())[:k]
        return ans