
nums = [-1, 1, 0, -3, 3]

n = len(nums)
answer = [0]*n
prefix = 1
for i in range(n):
    answer[i] = prefix
    prefix = prefix * nums[i]

postfix = 1
for j in range(n-1, -1, -1):
    answer[j] = answer[j]*postfix
    postfix = postfix * nums[j]

print(answer)
