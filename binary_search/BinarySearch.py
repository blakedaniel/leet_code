
nums = [num for num in range(100)]
target = 72
# output: 72


# nums = [-1,0,3,5,9,12]
# target = 9
# # output: 4

# nums = [-1,0,3,5,9,12]
# target = 2
# # output: -1

# nums = [5]
# target = 5
# # output: 0

# solved by slicing
def search1(nums: list[int], target: int) -> int:
    if len(nums) == 1:
        if nums[0] == target:
            return 0
        return -1
    middle_i = (len(nums) + 1)//2
    num = nums[middle_i]
    left = nums[: middle_i]
    right = nums[middle_i:]
    while num != target:
        if num > target:
            end = len(left)
            middle_i = (len(left) + 1)//2
            left = nums[:middle_i]
            right = nums[middle_i:end]
        else:
            start = middle_i
            middle_i += (len(right) + 1)//2
            left = nums[start:middle_i]
            right = nums[middle_i:]
        if len(left) == 0 or len(right) == 0:
            return -1
        num = nums[middle_i]
    return middle_i

# solved by redefining middle
def search2(nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        m = l + ((r - l)//2)
        print('LEFT:', l)
        print('MIDDLE:', m)
        print('RIGHT:', r)
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m
    return -1

search2(nums, target) 