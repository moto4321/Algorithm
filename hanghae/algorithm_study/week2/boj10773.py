# 제로
k = int(input())
stack = []
for _ in range(k):
    num = int(input())
    if num == 0 and len(stack) != 0:
        stack.pop()
    else:
        stack.append(num)

print(sum(stack))