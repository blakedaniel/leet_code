# def generateParenthesis(n: int) -> list[str]:
#     par = {
#         1: ['()'],
#         2: ['()()', '(())']
#     }

#     if n in (1, 2):
#         return par[n]
    
#     par_n = 3
#     while par_n <= n:
#         stackset = set()

#         for p in par[par_n - 1]:
#             # 2 + 1 | 1 + 2
#             stackset.add(p + par[1][0])
#             stackset.add(par[1][0] + p)

#             # 1 wrap 2
#         wrap_n = par_n//2
        
#         stackset.add(f'({p})')
#         par[par_n] = list(stackset)
#         par_n += 1
    
#     return par[n]

def generateParenthesis(n: int) -> list[str]:
    # if open_n < n, can add more opens
    # if closed_n < open_n, can add more opens
    # valid set IIF open_n = closed_n = n

    stack = []
    res = []

    # valid set IIF open_n = closed_n = n
    def backtrack(open_n, closed_n):
        breakpoint()
        if open_n == closed_n == n:
            res.append(''.join(stack))
            return
        
        if open_n < n:
            stack.append('(')
            backtrack(open_n + 1, closed_n)
            # breakpoint()
            stack.pop()

        if closed_n < open_n:
            stack.append(')')
            backtrack(open_n, closed_n + 1)
            # breakpoint()
            stack.pop()
        
    backtrack(0, 0)
    return res

print(generateParenthesis(4))