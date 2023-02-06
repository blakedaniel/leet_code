
def findDup(lst=[]):
    nums = {}
    for item in lst:
        nums[item] = nums.get(item, 0) + 1
        if nums[item] == 2:
            return True
    return False

findDup([1,2,3,1])
