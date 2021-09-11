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



# 1110 (int 방식)
n = int(input()) # 68

num = n
cnt = 0 # 사이클 수

while True:
    a = num // 10 # 6
    b = num % 10  # 8
    c = (a + b) % 10 # 6 + 8 = 1"4"
    num = b*10 + c

    cnt = cnt + 1
    if (num == n):
        break

print(cnt)

# 1110 (str 방식)
n = input()  # n = "26"

num = n
cnt = 0

while 1:
    if len(num) == 1:
        num = '0' + num
    plus = str(int(num[0]) + int(num[1])) # 2 + 6 = "8"
    num = num[-1] + plus[-1]
    cnt += 1
    if num == n:
        print(cnt)
        break


# 10818
n = input()
data = list(map(int, input().split()))

print(min(data), max(data))


# 2562
num_list = []

for i in range(9):
    num_list.append(int(input()))

print(max(num_list))
print(num_list.index(max(num_list))+1)

# 2577
a = int(input())
b = int(input())
c = int(input())

result = list(str(a*b*c))

for i in range(10):
    print(result.count(str(i)))


# 3052
arr = []
for i in range(10):
    n = int(input())
    arr.append(n % 42)

arr = set(arr)
print(len(arr))

# 1546
n = int(input())
test_list = list(map(int, input().split()))
max_score = max(test_list)

new_list = []
for score in test_list:
    new_list.append(score/max_score*100)
test_avg = sum(new_list)/n


# 8958
a = int(input())
for _ in range(a):
    ox = input()
    score = 0
    cnt = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            cnt += 1
            score += cnt
        elif ox[i] == 'X':
            cnt = 0
    print(score)


# 4344
n = int(input())

for _ in range(n):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:])/nums[0]  # 평균을 구함
    cnt = 0
    for score in nums[1:]:
        if score > avg:
            cnt += 1  # 평균 이상의 학생 수 
    rate = cnt/nums[0] * 100
    print(f'{rate: .3f}%')

# 함수
# 15596
def solve(a):
    return sum(a)


