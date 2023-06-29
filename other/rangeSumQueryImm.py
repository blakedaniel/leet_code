"""
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive 
where left <= right.

Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums 
between indices left and right inclusive 
(i.e. nums[left] + nums[left + 1] + ... + nums[right]).
"""
from itertools import accumulate

class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums
        self.prev_sums = {}
        
    def sumRange(self, left: int, right: int) -> int:
        nums = self.nums
        prev_sums = self.prev_sums
        
        if (left, right) in prev_sums:
            return prev_sums[(left, right)]
        else:
            curr_sum = sum(nums[left:right+1])
            prev_sums[(left, right)] = curr_sum
            return curr_sum
        

nums = [-2, 0, 3, -5, 2, -1]

nums = NumArray(nums)
print(nums.sumRange(0, 2))
print(nums.sumRange(2, 5))
print(nums.sumRange(0, 5))

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)