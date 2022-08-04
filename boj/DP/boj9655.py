# 돌 게임
n = int(input())
if n % 2 == 1:
    print('SK')
else:
    print('CY')


# 다른풀이
import sys
input = sys.stdin.readline
d = [-1] * 1001
d[1] = 1
d[2] = 0
d[3] = 1

for i in range(4, n + 1):
    if d[i - 1] or d[i - 3]:
        d[i] = 0
    else:
        d[i] = 1

print('CY' if dp[n] == 0 else 'SK')