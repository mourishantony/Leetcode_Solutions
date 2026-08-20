class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        store = Counter(arr1)
        ans = []
        for val in arr2:
            for i in range(store[val]):
                ans.append(val)
                arr1.remove(val)
        return ans + sorted(arr1)
