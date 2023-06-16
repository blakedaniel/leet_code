# input: array of ints nums, target that is being looked for, -bill to bill
# output: the indeces of two numbers that sum to target, solution is always possible
# order doesn't matter

# two sum unsorted, O(n)
def twoSum(target, nums=[]):
    # O(50n) = O(n)

    [3, 2, 1, 1]

    numIndexes = {}
    for i, num in enumerate(nums):
        if num not in numIndexes:
            numIndexes[num] = []

        numIndexes[num].append(i)

    numIndexes = {
        3: [0],
        2: [1],
        1: [2, 3]
    }

    for i, num in enumerate(nums):
        otherNum = target - num

        if otherNum in numIndexes:
            # pull out the other idnex
            #   otherIndex != i
            for otherIndex in numIndexes[otherNum]:
                if otherIndex != i:
                    return [i, otherIndex]

    pass


# # two sum sorted
# def twoSum(target, nums=[]):
#     nums.sort()
#     min_i = 0
#     max_i = len(nums) - 1
#     while min_i < max_i:
#         min = nums[min_i]
#         max = nums[max_i]
#         test_case = min + max

#         if target < test_case:
#             max_i -= 1
#         elif target > test_case:
#             min_i += 1
#         else:
#             return [max_i, min_i]


# nums1 = [-1] * 100000
# nums2 = [3] * 100000
# nums = nums1 + [1] + nums2
# target = 0

# twoSum(target, nums)
