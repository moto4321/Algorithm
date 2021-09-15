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


# 4673
# 1부터 10000까지 숫자 저장
num_set = set(range(1, 10001))

# 셀프 넘버가 아닌 수를 저장
not_self_num = set()

for i in range(1, 10001):
    for j in str(i): # 숫자를 문자열로 변환하여 102이면 1, 0, 2로 접근
        i += int(j)  # d(i) = i + j1 + j2 + j3 + .. = 102 + 1 + 0 + 2

    not_self_num.add(i) # 셀프 넘버가 아닌 수 저장

# 셀프 넘버만 있는 set = 전체 수 set - 셀프 넘버가 아닌 수 set
self_num = num_set - not_self_num

# 오름차순으로 정렬 후 출력
for i in sorted(self_num):
    print(i)

# 4673
이거 어렵다.

# 1065
num = int(input())
hansu = 0

for n in range(1, num +1):
    if n <= 99:
        hansu += 1
    else:
        nums = list(map(int, str(n)))
        if nums[0] - num[1] == nums[1] - nums[2]:
            hansu += 1

# 문자열
# 11654
a = input()
print(ord(a))

ord() : 문자를 아스키코드로 변환시켜줌
ord() 의 반대는 chr()

# 11710
    # 1 sum함수를 이용
n = input()
print(sum(map(int, input())))

    # 2 for문을 이용 -1
n = input()
nums = input()
total = 0
for i in nums :
    total += int(i)  # total= total+int(i)
print(total)

    # 3 for문을 이용 -2
n = input()
nums = input()
total = 0
for i in range(n) :  # 0부터 n-1까지
    total += int(nums[i])
print(total)


# 10809
word = input()
alphabet = list(range(97, 123))

for x in alphabet:
    print(word.find(chr(x)), end=" ")


# 2675
n = int(input())

for _ in range(n):
    cnt, word = input().split()
    for x in word:
        print(x*int(cnt), end=' ')
    print() # 줄넘김??


# 1157
words = input().upper()
unique_words = list(set(words)) # 입력받은 문자열에서 중복값을 제거

cnt_list = []
for x in unique_words:
    cnt = words.count(x)
    cnt_list.append(cnt) # count 숫자를 리스트에 append

if cnt_list.count(max(cnt_list)) > 1: # count 숫자 최대값이 중복되면
    print('?')
else:
    max_index = cnt_list.index(max(cnt_list)) # count 숫자 최대값 인덱스(위치)
    print(unique_words[max_index])

# 1152
n = input().split()
cnt = len(n)
print(cnt)
# split()과 split(" ") 차이 주의해야함!


# 2908
a, b = input().split()

a = int(a[::-1]) 
b = int(b[::-1])

if a > b : 
    print(a)
else :
    print(b)
