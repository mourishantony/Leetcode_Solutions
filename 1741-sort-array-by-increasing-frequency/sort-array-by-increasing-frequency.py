from collections import Counter, defaultdict


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        data = Counter(nums)
        nums_data = defaultdict(list)
        keys = list(data.keys())
        keys.sort()

        for key in keys:
            nums_data[data[key]].append(key)

        result = []

        keys = list(nums_data.keys())
        keys.sort()

        for key in keys:
            while nums_data[key]:
                res = nums_data[key].pop()
                n = data[res]
                while n > 0:
                    result.append(res)
                    n -= 1

        return result
