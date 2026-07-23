class NumArray:

    def __init__(self, nums: List[int]):
        self.Array = nums

    def sumRange(self, left: int, right: int) -> int:
        # print(self.Array[left : right])
        return sum(self.Array[left : right+1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)