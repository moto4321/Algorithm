# 다리 놓기
# 오답
import itertools
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    lst = [i for i in range(m)]

    nCr = itertools.combinations(lst, m - n)
    print(len(list(nCr)))



# 다른사람 풀이
def factorial(num):
    if num < 2:
        return 1
    else:
        return num * factorial(num - 1)

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(factorial(m) // (factorial(n) * factorial(m - n)))