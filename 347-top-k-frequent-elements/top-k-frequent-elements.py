class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) ==1:
            return nums
        store = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]

        for key , value in store.items():
            bucket[value].append(key)
        ans =[]
        for key in range(len(nums),0,-1):
            for num in bucket[key]:
                ans.append(num)

                if len(ans) == k:
                    return ans
