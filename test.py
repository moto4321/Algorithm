# 3052

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())
g = int(input())
h = int(input())
i = int(input())
j = int(input())

arr = [a, b, c, d, e, f, g, h, i, j]
answer = []
count = 0

for m in range(len(arr)):
    k = arr[m]%42
    answer.append(k)

for n in answer:
    ans = n
    if n != ans:
        count += 1


print(count)