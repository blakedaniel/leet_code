# Given an integer array nums, return an array answer such that answer[i]
# is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a
# You must write an algorithm that runs in O(n) time
# and without using the division operation.

nums = [1,2,3,4] # --> [24,12,8,6]
# nums = [-1,1,0,-3,3] # --> [0,0,9,0,0]
# [a, b, c, d] --> [b*c*d, a*c*d, a*b*d, a*b*c]


def productExceptSelf1(nums: list[int]) -> list[int]:
    multmap = [1] * len(nums)

    growing_mult = 1
    for n in range(len(nums)):
        multmap[n] *= growing_mult
        growing_mult *= nums[n]
    
    multmap.reverse()
    nums.reverse()

    growing_mult = 1
    for n in range(len(nums)):
        multmap[n] *= growing_mult
        growing_mult *= nums[n]
    
    multmap.reverse()
    return multmap

productExceptSelf1(nums)