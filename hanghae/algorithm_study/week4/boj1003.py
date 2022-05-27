# 이건 내풀이 - 시간초과
import sys
input = sys.stdin.readline
t = int(input())

def fibo(num):
    global zero_cnt, one_cnt
    if num == 0:
        zero_cnt += 1
        return 0
    elif num == 1:
        one_cnt += 1
        return 1
    return fibo(num - 1) + fibo(num - 2)

for _ in range(t):
    zero_cnt = 0
    one_cnt = 0
    n = int(input())
    fibo(n)
    print(zero_cnt, one_cnt)

# 답안
t = int(input())
for _ in range(t):
    n = int(input())
    zero_cnt = 1
    one_cnt = 0
    tmp = 0
    for _ in range(n):
        tmp = one_cnt
        one_cnt += zero_cnt
        zero_cnt = tmp
    print(zero_cnt, one_cnt)

# 답안2
zero = [1, 0, 1]
one = [0, 1, 1]

def fibo(num):
    length = len(zero)
    if num >= length:
        for i in range(length, num + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    print('{} {}'.format(zero[num], one[num]))

t = int(input())
for _ in range(t):
    fibo(int(input()))
