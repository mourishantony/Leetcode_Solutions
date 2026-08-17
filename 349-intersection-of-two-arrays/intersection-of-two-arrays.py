class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) >= len(nums2):
            s = nums2
            l = nums1
        else:
            s = nums1
            l = nums2

        l = set(l)
        ans =set()
        for num in s:
            if num in l:
                ans.add(num)
        return list(ans)