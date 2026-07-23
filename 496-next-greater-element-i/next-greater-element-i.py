class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}

        for num in nums2:
            while stack and num > stack[-1]:
                popped = stack.pop()
                hashmap[popped] = num
            stack.append(num)
        
        while stack:
            popped = stack.pop()
            hashmap[popped] = -1

        ans = []

        for num in nums1:
            ans.append(hashmap[num])
        
        return ans
