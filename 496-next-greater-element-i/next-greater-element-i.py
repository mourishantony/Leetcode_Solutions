class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            if index == len(nums2) -1:
                ans.append(-1)
            else:
                for j in nums2[index+1:]:
                    if j > nums2[index]:
                        ans.append(j)
                        break
                    if j < nums2[index] and j == nums2[-1]:
                        ans.append(-1)
        return ans