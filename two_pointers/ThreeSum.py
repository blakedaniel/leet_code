# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
from time import time

tests = (
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0,1,1], []),
    ([0,0,0], [[0,0,0]])
)

def threeSum1(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    # nums = [-4, -1, -1 0, 1, 2]
    for i in range(len(nums) - 2):
        anchor = nums[i]
        lesser_i = i + 1
        greater_i = len(nums) - 1
        
        while lesser_i < greater_i:
            if anchor + nums[lesser_i] + nums[greater_i] > 0:
                greater_i -= 1
            elif anchor + nums[lesser_i] + nums[greater_i] < 0:
                lesser_i += 1
            else:
                zero = [anchor, nums[lesser_i], nums[greater_i]]
                if zero not in res:
                    res.append(zero)
                lesser_i += 1
    return list(res)




funcs = (threeSum1,)

def check(funcs, tests):
    for func in funcs:
        stime = time()
        for _input, _output in tests:
            result = func(_input)
            correct = func(_input) == _output
            if correct:
                print(f'{_input}: {correct}')
            else:
                print(f'\n{_input}: {correct}')
                print(f'Expected Result: {_output}')
                print(f'Produced Result: {result}')
                print('\n')
        ttime = time() - stime
        print('Run Time: ', ttime, '***********\n')

check(funcs, tests)