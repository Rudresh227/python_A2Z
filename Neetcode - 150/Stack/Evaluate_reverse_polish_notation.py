from typing import List

def evalRPN(tokens: List[str]) -> int:
    stack = []

    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())

        elif token == "-":
            b = stack.pop()
            a = stack.pop()
            stack.append(a - b)

        elif token == "*":
            stack.append(stack.pop() * stack.pop())

        elif token == "/":
            a = stack.pop()
            b = stack.pop()
            stack.append(int(b / a))  # truncate toward zero

        else:
            stack.append(int(token))

    return stack[0]

tokens = ["2", "1", "+", "3", "*"]
print(evalRPN(tokens))  # Output: 9

tokens = ["4","13","5","/","+"]
print(evalRPN(tokens))  # Output: 6

