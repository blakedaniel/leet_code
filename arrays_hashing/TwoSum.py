# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.

import time

test = (
    ([2,7,11,15], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6, [0,1])
)


# by window approach
def twoSum1(nums: list[int], target: int) -> list[int]:
    for i in range(len(nums)):
        num1 = nums[i]
        batch = nums[i+1:]
        while batch:
            num2 = batch.pop()
            sum_num = num1 + num2
            if sum_num == target:
                return [i, len(batch) + (1 + i)]

# by hashmap
def twoSum2(nums: list[int], target: int) -> list[int]:
    prevMap = {} # map of all previously looped through nums; num -> index
    for i, num in enumerate(nums):
        if (target - num) in prevMap:
            return [i, prevMap[target - num]]
        prevMap[num] = i

funcs = (twoSum1, twoSum2)

for func in funcs:
    stime = time.time()
    for nums, target, output in test:
        print(func(nums, target), output, nums)
    ttime = time.time() - stime
    print('Run Time: ', ttime, '\n')
