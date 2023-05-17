
def calculate(expression):
    operations_stack = []
    operators = {
        '+': '+', 'add': '+',
        '-': '-', 'sub': '-',
        '*': '*', 'mul': '*',
        '/': '/', 'div': '/',
    }

    for item in expression.split()[::-1]:
        if item.isdecimal() or item.lstrip('-').replace('.', '', 1).isdecimal():
            operations_stack.append(item)
        elif item in operators and len(operations_stack) > 1:
            result = eval(f'{operations_stack.pop()}{item}{operations_stack.pop()}')
            operations_stack.append(result)
        else:
            raise ValueError('Invalid expression')

    if len(operations_stack) > 1:
        raise ValueError('Invalid expression')

    return operations_stack[0]


print(calculate('+ 2 3'))  # 5
print(calculate('* 6 + 4 5'))  # 54
print(calculate('+ - / 7 5 6 - 4 6'))  # 54

print(calculate("+ - * 2 3 3 / / 8 4 + 1 1"))  # 2×3−3+8/4/(1+1) = 4.0