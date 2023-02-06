
#target = 2
# numbers = ([-1] * (10 ** 5)) + [1, 1] + ([10] * (10 ** 4))
# target = 0
# numbers = [0, 0, 1, 7]
# target = 9
# numbers = [2, 7, 11, 15]
# target = 15
# numbers = [1, 2, 3, 12, 25, 50]
target = 100
numbers = [5, 25, 75]


def twoSum(numbers=[], target=0):
    checked = set()
    for i, _ in enumerate(numbers):
        if numbers[i] not in checked:
            comp = target - numbers[i]
            print(numbers[i], comp)
            if comp in numbers[i+1:]:
                return[i + 1, numbers[i+1:].index(comp) + (i + 2)]
            checked = checked.union({numbers[i], comp})


twoSum(numbers, target)
