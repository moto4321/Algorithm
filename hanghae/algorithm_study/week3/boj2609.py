n, m = map(int, input().split())

lst_n = []
lst_m = []

for i in range(1, n // 2 + 1):
    if n % i == 0:
        lst_n.append(i)

for i in range(1, m // 2 + 1):
    if m % i == 0:
        lst_m.append(i)

gcd = 0
lcm = 0
for num in lst_n:
    if num in lst_m:
        gcd = num

sml_num = min(n, m)
big_num = max(n, m)
i = 1
while True:
    if big_num * i % sml_num == 0:
        lcm = big_num * i
        break
    i += 1


print(gcd)
print(lcm)

# 유클리드 호제법
a, b = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))


# 파이썬 3.9 부터 내장함수 지원...
import math

a, b = map(int, input().split())

print(math.gcd(a, b))
print(math.lcm(a, b))