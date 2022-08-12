# 계단 오르기
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

d = []

d.append(lst[0])
d.append(max(lst[0] + lst[1], lst[1]))
d.append(max(lst[0] + lst[2], lst[1] + lst[2]))
for i in range(3, n):
    d.append(max(d[i - 2] + lst[i], d[i - 3] + lst[i] + lst[i - 1]))

print(d.pop())