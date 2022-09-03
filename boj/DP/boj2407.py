# 조합
n, m = map(int, input().split())

a, b, c = 1, 1, 1
for i in range(1, n + 1):
    a *= i

for i in range(1, n - m + 1):
    b *= i

for i in range(1, m + 1):
    c *= i

print(round(a // (b * c)))



# factorial 사용
import math
n, m = map(int, input().split())
up = math.factorial(n)
down = (math.factorial(n - m)) * (math.factorial(m))
print(up // down)