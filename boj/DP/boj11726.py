# 2xN 타일링
n = int(input())

d = [0] * (n + 1)

d[1] = 1
if n > 1:
    d[2] = 2
if n > 2:
    d[3] = 3

if len(d) > 3:
    for i in range(4, len(d)):
        d[i] = d[i - 1] + d[i - 2]

print(d[len(d) - 1] % 10007)


# 더 나은 풀이
d = [0, 1, 2]
for i in range(3, 1001):
    d.append(d[i - 2] + d[i - 1])
n = int(input())
print(d[n] % 10007)