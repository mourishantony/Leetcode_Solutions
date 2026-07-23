class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def bubble_sort(nums):
            flag = True

            while flag:
                flag = False
                for i in range(1,len(nums)):
                    if nums[i-1] > nums[i]:
                        flag = True
                        nums[i-1],nums[i] = nums[i] , nums[i-1]

        def insertion_sort(nums):
            n = len(nums)
            for i in range(1,n):
                for j in range(i,0,-1):
                    if nums[j-1] > nums[j]:
                        nums[j-1] ,nums[j] = nums[j] , nums[j-1]
                    else:
                        break

        def selection_sort(nums):
            n = len(nums)
            for i in range(n):
                for j in range(i+1,n):
                    if nums[i] > nums[j]:
                        nums[i] , nums[j] = nums[j] , nums[i]

        def merge_sort(nums):
            n = len(nums)
            if n < 2:
                return nums
            
            m = n//2
            L = nums[:m]
            R = nums[m:]

            L = merge_sort(L)
            R = merge_sort(R)

            l,r = 0,0
            L_len = len(L)
            R_len = len(R)

            i = 0
            sorted_arr = [0] *n

            while l < L_len and r < R_len:
                if L[l] <= R[r]:
                    sorted_arr[i] = L[l]
                    l+=1
                else:
                    sorted_arr[i] = R[r]
                    r+=1
                i+=1
            
            while l < L_len:
                sorted_arr[i] = L[l]
                l+=1
                i+=1
            while r < R_len:
                sorted_arr[i] = R[r]
                r+=1
                i+=1

            return sorted_arr

        # bubble_sort(nums)
        # insertion_sort(nums)
        # selection_sort(nums)
    
        return merge_sort(nums)