# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.
# You must write a solution in O(log(m * n)) time complexity.
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
# Output: false

# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target = 3
# # Output: true

# matrix = [[1]]
# target = 0
# # output: false

# matrix = [[1]]
# target = 1
# # output: true


def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    top = 0
    bottom = len(matrix) - 1
    row = 0
    while top <= bottom:
        row = top + (bottom - top)//2
        if target < min(matrix[row]):
            bottom = row - 1
        elif target > max(matrix[row]):
            top = row + 1
        else:
            break
        
    row = matrix[row]
    l = 0
    r = len(row) - 1
    while l <= r:
        m = l + (r - l)//2
        if target < row[m]:
            r = m - 1
        elif target > row[m]:
            l = m + 1
        else:
            break
    return target == row[m]


searchMatrix(matrix, target)