# # via while loops -- not the fastest or completest way
# def evalRPN(tokens: list[str]) -> int:
#     pre_operator = []
#     while len(tokens) != 0:
#         # [x] identify where the first operater is
#         while tokens[0] not in ('+', '-', '*', '/'):
#             pre_operator.append(tokens.pop(0))
#             # [x] split into two groups tokens1 (with target operator) and tokens2 (without)
#         batch = [int(pre_operator[-2]), int(pre_operator[-1])] + [tokens.pop(0)]
#         # breakpoint()
#         pre_operator = pre_operator[:-2]
#             # [x] pluck operator and two proceeding ints from tokens1
#             # [x] calculate based on 3
#         match batch[2]:
#             case '+':
#                 token = batch[0] + batch[1]
#             case '-':
#                 token = batch[0] - batch[1]
#             case '*':
#                 token = batch[0] * batch[1]
#             case '/':
#                 if -1 < batch[0] / batch[1] < 0:
#                     token = 0
#                 else:
#                     token = batch[0] // batch[1]

#         # [x] add output back at start of list
#         pre_operator.append(str(token))
#         # [x] repeat until list contains 1 digit
#         # breakpoint()
#     return int(pre_operator[0])


def evalRPN(tokens: list[str]) -> int:
    token_stack = []
    for c in tokens:
        if c not in ('+', '-', '*', '/'):
            token_stack.append(int(c))
        else:
            match c:
                case '+':
                    token_stack.append(token_stack.pop() + token_stack.pop())
                case '-':
                    second, first = token_stack.pop(), token_stack.pop()
                    token_stack.append(first - second)
                case '*':
                    token_stack.append(token_stack.pop() * token_stack.pop())
                case '/':
                    second, first = token_stack.pop(), token_stack.pop()
                    token_stack.append(int(first / second))
    return token_stack[0]


# tokens = ["2","1","+","3","*"]
# tokens = ["4","13","5","/","+"]
tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
print(evalRPN(tokens))