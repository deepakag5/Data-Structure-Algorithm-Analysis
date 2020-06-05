def evalReversePolish(tokens):
    if len(tokens) == 1:
        return tokens[0]
    if len(tokens) == 0:
        return None

    stack = []
    operators_map = ["+", "-", "*", "/"]

    for t in tokens:
        if t not in operators_map:
            stack.append(int(t))
        else:
            r, l = stack.pop(), stack.pop()
            if t == "+":
                stack.append(l + r)
            elif t == "-":
                stack.append(l - r)
            elif t == "*":
                stack.append(l * r)
            else:
                stack.append(int(float(l) / r))  # truncates value of x to -1<x<0 to 0

    return stack[0]


def evalRPN(tokens):
    if len(tokens) == 1:
        return tokens[0]
    if len(tokens) == 0:
        return None

    stack = []
    operators_map = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: int(x / y)
    }

    for t in tokens:
        if t in operators_map:
            stack.append(operators_map[t](stack.pop(), stack.pop()))
        else:
            stack.append(int(t))

    return stack[0]

# def evalReversePol(tokens):
#     stack = []
#
#     if len(tokens) == 1:
#         return tokens[0]
#     if len(tokens) == 0:
#         return None
#
#     for item in tokens:
#         if item not in ['+', '-', '*', '/']:
#             stack.append(int(item))
#         else:
#             num2 = stack.pop()
#             num1 = stack.pop()
#             if item == '+':
#                 stack.append(num1 + num2)
#             if item == '-':
#                 stack.append(num1 - num2)
#             if item == '*':
#                 stack.append(num1 * num2)
#             if item == '/':
#                 stack.append(int(num1 / num2))
#     return stack.pop()


# def evalRPN(self, tokens: List[str]) -> int:
#     if not tokens:
#         return 0
#     stack = []
#     for token in tokens:
#         if token in self.operators:
#             stack.append(self.operators[token](stack.pop(), stack.pop()))
#         else:
#             stack.append(int(token))
#     return stack[0]
#
# def __init__(self):
#     self.operators = {
#         '+': lambda y, x: x + y,
#         '-': lambda y, x: x - y,
#         '*': lambda y, x: x * y,
#         '/': lambda y, x: int(x / y)
#     }
