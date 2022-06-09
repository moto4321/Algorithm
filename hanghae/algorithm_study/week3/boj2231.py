n = int(input())

num = str(n - 27)
answer = 0
while True:
    lst = []
    for i in num:
        lst.append(int(i))
    if int(num) + sum(lst) == n:
        answer = int(num)
        break
    num = str(int(num) + 1)
    if int(num) == n:
        break

if int(num) == n:
    print(0)
else:
    print(answer)


# 다른 사람 풀이
n = int(input())
result = 0

for i in range(1, n + 1):
    a = list(map(int, str(i)))
    s = i + sum(a)
    if s == n:
        result = i
        break

print(result)

# 또 다른 풀이
n = int(input())
result = 0

for i in range(1, n + 1):
    tmp = i + sum(map(int, str(i)))
    if tmp == n:
        result = i
        break

print(result)