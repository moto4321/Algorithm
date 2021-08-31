# 8393
data = int(input())

result = 0

for i in range(1, data+1):
    result += i

print(result)


# 15552

# 2741
n = int(input())

for i in range(1, n+1):
    print(i)

# 2742
n = int(input())

for i in range(n, 0, -1):
    print(i)

# 11021
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    ans = a + b
    print("case#%s: %s" %(i+1, ans))


# 11022
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    ans = a + b
    print("Case #%s: %s + %s = %s" %(i+1, a, b, ans))

# 2438
n = int(input())

for i in range(n):
    print('*' * i)

# 2439
n = int(input())

for i in range(n):
    print(' ' * (n-i-1),'*' * (i+1))

# 10871
n, x = map(int, input().split())

a = list(map(int, input().split()))

for i in range(n):
    if a[i] < x:
        print(a[i], end=" ")



# 10952
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)



# 10951
# 풀이1
while 1:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break

# 풀이2
try:
    while 1:
        a, b = map(int, input().split())
        print(a + b)
except:
    exit()