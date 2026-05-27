class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        

    def sumRange(self, left: int, right: int) -> int:
        self.left = left
        self.right = right
        Sum = 0
        for i in range(self.left, self.right + 1):
            Sum += self.nums[i]
        
        return Sum
    
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)