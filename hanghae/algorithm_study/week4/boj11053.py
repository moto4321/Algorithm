# 가장 긴 증가하는 부분 수열
n = int(input())
lst = list(map(int, input().split()))

new_lst = [lst[0]]
for i in range(1, len(lst)):
    if lst[i] > lst[i - 1]:
        new_lst.append(lst[i])

print(len(new_lst))
# 틀림... 왜...

# 다른 사람 풀이
n = int(input())

lst = list(map(int, input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if lst[j] < lst[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))