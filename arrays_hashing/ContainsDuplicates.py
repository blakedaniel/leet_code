# check if array contains duplicates
# return true if does, else false

# nums = [1,2,3,1]
# nums = [1,2,3,4]
nums = [1,1,1,3,3,4,3,2,4,2]

# # by set length
# def containsDuplicate(nums: list[int]) -> bool:
#     return not len(nums) == len(set(nums))

# # by counting
# def containsDuplicate(nums: list[int]) -> bool:
#     count = {}
#     for num in nums:
#         count[num] = count.get(num, 0) + 1
#         if 2 in count.values():
#             return True
#     return False

# by hashset (FINAL)
def containsDuplicate(nums: list[int]) -> bool:
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        else:
            hashset.add(num)
    return False

containsDuplicate(nums)