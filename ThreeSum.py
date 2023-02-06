# Given an integer array nums, return all the triplets[nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums):
    triplets = []
    nums.sort()
    for i, num in enumerate(nums):
        li = i + 1
        ri = len(nums) - 1
        z = num
        while li < ri and num < 1:
            lx = nums[li]
            ry = nums[ri]
            if lx + ry + z > 0:
                ri -= 1
            elif lx + ry + z < 0:
                li += 1
            else:
                li += 1
                if [num, lx, ry] not in triplets:
                    triplets.append([num, lx, ry])
                while nums[li - 1] == nums[li] and li < ri:
                    li += 1
    return triplets


test = [0, 0, 0]
# test = [0, 0, 0, 0]
# test = [0, 1, 1]
# test = [-1, 0, 1, 2, -1, -4]

s = threeSum(test)

for item in s:
    print(item)
