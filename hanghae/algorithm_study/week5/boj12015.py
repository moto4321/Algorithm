# 가장 긴 증가하는 부분 수열2
import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))

dp = [0]

for i in range(n):
    start = 0
    end = len(dp) - 1
    while start <= end:
        mid = (start + end) // 2
        if dp[mid] < lst[i]:
            start = mid + 1
        else:
            end = mid - 1
    if start >= len(dp):
        dp.append(lst[i])
    else:
        dp[start] = lst[i]

print(len(dp) - 1)


# keyword : bisect

# bisect를 사용한 풀이
import sys
input = sys.stdin.readline
from bisect import bisect_left

n = int(input())
lst = list(map(int, input().split()))

dp = [0]

for i in lst:
    if dp[-1] < i:
        dp.append(i)
    else:
        dp[bisect_left(dp, i)] = i

print(len(dp) - 1)