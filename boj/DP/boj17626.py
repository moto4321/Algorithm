# Four Squares
import sys
input = sys.stdin.readline
n = int(input())

d = [-1] * 50001
d[1] = 1
d[2] = 2
d[3] = 3

d[4] = 1

d[5] = 2
d[6] = 3 # 2^2 + 1^1 + 1^1
d[7] = 4 # 2^2 + 1^1 + 1^1 + 1^1
d[8] = 2 # 2^2 + 2^2

d[9] = 1

d[10] = 2
d[11] = 3
d[12] = 4
d[13] = 2
d[14] = 3 # 9 + 4 + 1
d[15] = 4 # 9 + 4 + 1 + 1

d[16] = 1

# 규칙을 못찾겠다...
# n - (n보다 작거나 같은 제곱수) 를 index로 갖는 값에 1을 더해주면된다.

# DP
n = int(input(0))
d = [0, 1]

for i in range(2, n + 1):
    min_value = 1e9
    j = 1
    while (j ** 2) <= i:
        min_value = min(min_value, d[i - (j ** 2)])
        j += 1
    d.append(min_value + 1)
print(d[n])
