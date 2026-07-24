class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            n= len(nums)
            if n < 2:
                return nums
            
            m = n//2
            L,R = nums[:m] , nums[m:]

            L = merge_sort(L)
            R = merge_sort(R)

            l,r,i = 0,0,0
            sorted_nums = [0]*n

            while l < len(L) and r < len(R):
                if L[l] < R[r]:
                    sorted_nums[i] = L[l]
                    l+=1
                else:
                    sorted_nums[i] = R[r]
                    r+=1
                i+=1

            while l < len(L):
                sorted_nums[i] = L[l]
                l+=1
                i+=1
            
            while r < len(R):
                sorted_nums[i] = R[r]
                r+=1
                i+=1

            return sorted_nums

        ans = merge_sort(nums)
        return ans