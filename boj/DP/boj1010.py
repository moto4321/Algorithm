# 다리 놓기
t = int(input())

def factorial(num):
    if num < 2:
        return 1
    return num * factorial(num - 1)

for _ in range(t):
    a, b = map(int, input().split())
    print(factorial(b) // (factorial(a) * factorial(b - a)))