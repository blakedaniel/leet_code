def TwoSum(nums:list, target:int):
    prevs = {}
    for index, num in enumerate(nums):
        if num in prevs:
            return index, prevs[num]
        prevs[target - num] = index
    
# write function that wraps around TwoSum and return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Also the solution set must not contain duplicate triplets.
def ThreeSum(nums:list):
    triplets = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            k = TwoSum(nums, -(nums[i] + nums[j]))
            if k:
                triplet = sorted([nums[i], nums[j], nums[k[0]]])
                if triplet not in triplets:
                    triplets.append(triplet)
    return triplets