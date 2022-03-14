# 내 풀이

n = int(input())

for _ in range(n):
    x = input()
    # stack = []
    sum = 0
    for par in x:
        if par == '(':
            sum += 1
        else:
            sum -= 1
            if sum < 0:
                print('NO')
                break


    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')


# 스택을 이용한 풀이

n = int(input())

for _ in range(n):
    x = input()
    stack = []
    for par in x:
        if par == '(':
            stack.append(par)
        else:
            if not stack:
                print('NO')
                break
            last = stack.pop()
            if last != '(':
                break
    else: # break문으로 끊기지 않고 수행됐을 경우 수행한다.
        if not stack:
            print('YES')
        else:
            print('NO')