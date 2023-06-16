# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing
# order, find two numbers such that they add up to a specific target number. Let these 
# two numbers be numbers[index1] and numbers[index2]
# where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer
# array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution.
# You may not use the same element twice.
# Your solution must use only constant extra space.

import time

test = (
    # ([2,7,11,15], 9, [1,2]),
    # ([2,3,4], 6, [1,3]),
    # ([-1,0], -1, [1,2]),
    ([0,0,3,4], 0, [1, 2]),
)


def twoSum1(numbers: list[int], target: int) -> list[int]:
    res = None
    lesser_i, greater_i = 0, len(numbers) - 1
    while res != target:
        res = numbers[lesser_i] + numbers[greater_i]
        if res < target:
            lesser_i += 1
        elif res > target:
            greater_i -= 1
    return [lesser_i + 1, greater_i + 1]


def twoSum2(numbers: list[int], target: int) -> list[int]:
    lesser_i, greater_i = 0, len(numbers) - 1
    while lesser_i < greater_i:
        if numbers[lesser_i] + numbers[greater_i] > target:
            greater_i -= 1
        elif numbers[lesser_i] + numbers[greater_i] < target:
            lesser_i += 1
        else:
            return [lesser_i + 1, greater_i + 1]

funcs = (twoSum1, twoSum2)

for func in funcs:
    stime = time.time()
    for nums, target, output in test:
        print(func(nums, target), output, nums)
    ttime = time.time() - stime
    print('Run Time: ', ttime, '\n')