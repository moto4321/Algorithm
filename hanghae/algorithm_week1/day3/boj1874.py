n = int(input())
stack = []
answer = []
flag = 0
cur = 1
for i in range(n):
    num = int(input()) # num =
    while cur <= num:  # cur = 9  /  # num = 8
        stack.append(cur)  # stack = [1, 2, 5, 6, 7, 8]
        answer.append('+')
        cur += 1 # cur = 9
    # 입력한 수를 만나면 while문 탈출. 즉, cur = num 일 때까지 while문을 돌아 스택에 쌓는다.

    if stack[-1] == num: # stack = [1, 2, 5, 6, 7, 8]   /   num = 8
        stack.pop() # stack = [1, 2, 5, 6, 7]
        answer.append('-')
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)