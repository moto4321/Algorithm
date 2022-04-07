# 퇴사

"""
dp(n번째 날, 여태까지 번 돈)
    -> 근무를 한다면 dp(n + t, 여태까지번돈, + n번쨰날에 번돈)
    -> 근무를 안한다면 dp(n + 1, 여태까지번돈)
"""

n = int(input())
lst = []
for _ in range(n):
    # 소요일수, 돈
    a, b = map(int, input().split())
    lst.append((a, b))

print(lst)
max_pay = 0

def dp(idx, pay):
    global max_pay
    if idx >= n:
        if pay > max_pay:
            max_pay = pay
        return

    t, p = lst[idx]

    for i in range(2):
        if i == 1:
            if idx + t > n:
                return
            dp(idx + t, pay + p)
        else:
            dp(idx + 1, pay)


dp(0, 0)
print(max_pay)