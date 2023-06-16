
# target = 2
# numbers = ([-1] * (10 ** 5)) + [1, 1] + ([10] * (10 ** 4))
# target = 0
# numbers = [0, 0, 1, 7]
# target = 9
# numbers = [2, 7, 10, 15]
target = 15
numbers = [1, 2, 3, 12, 25, 50]

'''for i, n in enumerate(numbers):
    comp = target - n
    comp_check = numbers[i+1:].count(comp)
    if comp_check != 0:
        j = numbers[i+1:].index(comp)
        print([i+1, j+i+2])'''


def twoSum(numbers=[], target=0):
    for i in range(0, len(numbers)):
        l_num =
