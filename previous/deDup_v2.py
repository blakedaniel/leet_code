
def findDup(lst=[]):
    nums = {}
    for item in lst:
        if item in nums:
            return True
        else:
            nums[item] = 'BOOOOOO'
    return False

findDup([1,2,3,1])
