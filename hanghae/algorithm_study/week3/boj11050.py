# 이항 계수1
n, k = map(int, input().split())

def factorial(x):
    ans = 1
    for i in range(2, x + 1):
        ans *= i
    return ans

print(factorial(n) // factorial(k) // factorial(n - k))
