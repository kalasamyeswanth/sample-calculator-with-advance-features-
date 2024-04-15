import re

def calculate(expression):
    # Define a regular expression pattern to extract numbers, operators, and parentheses
    pattern = r'(\d+\.?\d*)|([-+*/^()])'
    tokens = re.findall(pattern, expression)

    # Convert infix expression to postfix using the shunting yard algorithm
    output = []
    stack = []
    precedence = {'^': 3, '*': 2, '/': 2, '+': 1, '-': 1, '(': 0}

    for token in tokens:
        if token[0].isdigit():
            output.append(token[0])
        elif token[0] == '(':
            stack.append(token[0])
        elif token[0] == ')':
            while stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence[token[0]] <= precedence[stack[-1]]:
                output.append(stack.pop())
            stack.append(token[0])

    while stack:
        output.append(stack.pop())

    # Evaluate the postfix expression
    stack = []
    for token in output:
        if token.isdigit():
            stack.append(float(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '^':
                stack.append(a ** b)

    return stack[0]

# Test the calculator
expression = input("Enter an expression to evaluate: ")
result = calculate(expression)
print("Result:", result)
