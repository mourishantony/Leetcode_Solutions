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

        temp = [0] * len(nums)

        def merge_sort(left, right):
            if left >= right:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid + 1, right)

            i = left
            j = mid + 1
            k = left

            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp[k] = nums[i]
                    i += 1
                else:
                    temp[k] = nums[j]
                    j += 1
                k += 1

            while i <= mid:
                temp[k] = nums[i]
                i += 1
                k += 1

            while j <= right:
                temp[k] = nums[j]
                j += 1
                k += 1

            for i in range(left, right + 1):
                nums[i] = temp[i]

        merge_sort(0, len(nums) - 1)

        # bubble_sort(nums)
        # insertion_sort(nums)
        # selection_sort(nums)
    
        return nums