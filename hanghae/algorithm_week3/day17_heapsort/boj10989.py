# 수 정렬하기3

import sys
input = sys.stdin.readline
n = int(input())
check_lst = [0] * 10001

for _ in range(n):
    num = int(input())
    check_lst[num] += 1

for i in range(10001):
    if check_lst[i] != 0:
        for _ in range(check_lst[i]):
            print(i)


# 아무리 해도 메모리 초과...