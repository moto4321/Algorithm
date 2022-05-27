while True:
    sentence = input()
    if sentence == '.':
        break
    stack = []
    flag = True
    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif char == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break

    if len(stack) != 0:
        print('no')
    elif len(stack) == 0:
        print('yes')
