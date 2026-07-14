import re

from RPN.rpn import precedence

prec= {'+' : 1, '-' : 1, '*': 2, '/': 2, 'u-': 3, 'u+' : 3}

def is_unary(t, prev):
    if prev is None or prev in ['(', '+', '-', '*', '/']:
        return True

    return False

def add_to_stack(t, stack, out):
    if not stack or stack[-1] == '(':
        stack.append(t)
        return

    if t in ['u+', 'u-']:  # right associativity case
        while stack and stack[-1] != '(' and prec[stack[-1]] > prec[t]: # strictly greater
            out.append(stack[-1])
            stack.pop()
    else:
        while stack and stack[-1] != '(' and prec[stack[-1]] >= prec[t]:
            out.append(stack[-1])
            stack.pop()

    stack.append(t)

def shunting_yard(s):
    tokens = re.findall(r'\d+|[*/+\-()]', s)
    print(f"{tokens}")

    prev, stack, out = None, [], []

    for t in tokens:
        if t == '(':
            stack.append(t)

        if t == ')':
            while stack[-1] != '(':
                out.append(stack[-1])
                stack.pop()
            stack.pop()

        elif t.isdigit():
            out.append(t)

        elif t in ['+', '-', '*', '/']:
            if is_unary(t, prev):
                add_to_stack('u' + t, stack, out)
            else:
                add_to_stack(t, stack, out)

        prev = t

    while stack:
        out.append(stack.pop())

    return out

def evaluate(tokens):
    stack = []
    for t in tokens:
        if t.isdigit():
            stack.append(int(t))
        elif t == 'u-':
            stack.append(-1 * stack.pop())
        elif t == 'u+':
            stack.append(stack.pop())
        elif t == '+':
            first = stack.pop()
            second = stack.pop()
            stack.append(first + second)
        elif t == '-':
            first = stack.pop()
            second = stack.pop()
            stack.append(second - first)
        elif t == '*':
            first = stack.pop()
            second = stack.pop()
            stack.append(first * second)
        elif t == '/':
            first = stack.pop()
            second = stack.pop()
            stack.append(second//first)

    result = stack.pop()
    if stack:
        raise ValueError(f"Malformed expression: leftover stack {stack}")
    return result

def main():
    expr = '-2 * -(-3 + 5)'
    print(f'{expr}')

    out = shunting_yard(expr)
    print(f"{out}")

    out = evaluate(out)
    print(f"{out}")


if __name__ == "__main__":
    main()