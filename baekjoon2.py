# 기본 수학 1
# 1712
A, B, C = map(int, input().split())

if B>=C:
    print(-1)
else:
    print(int(A/(C-B)+1))


#2292
n = int(input())

nums_pileup = 1 # 벌집의 개수, 1개부터 시작
cnt = 1
while n > nums_pileup:
    nums_pileup += 6*cnt # 벌집이 6의 배수로 증가
    cnt += 1 # 반복문을 반복하는 횟수
print(cnt)


# 1193
n = int(input())
line = 1

while n > line:
    n -= line
    line += 1

if line % 2 == 0:
    a = n
    b = line - n + 1
else:
    a = line - n + 1
    b = n

print(a, "/", b, sep="")


# 2869
import sys
import math

a, b, v = map(int, sys.stdin.readline().split())

day = (v - b) / (a - b)
print(math.ceil(day))

# 10250
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    h,w,n = map(int, sys.stdin.readline().split())

    if n % h == 0:
        flr = h
        num = n // h
    else:
        flr = n % h
        num = n // h + 1

    print(f'{flr*100 + num}')

# 2775
t = int(input())

for _ in range(t):
    floor = int(input()) # 층
    num = int(input()) # 호

    f0 = [x for x in range(1, num + 1)] # 0층 리스트
    
    for k in range(floor): # 층 수 만큼 반복
        for i in range(1, num): # 1 ~ n-1까지 (인덱스로 사용)
            f0[i] += f0[i-1] # 층별 각 호실의 사람 수를 변경
    print(f0[-1]) # 가장 마지막 수 출력


# 2839 다시 풀기..
n = int(input()) # 설탕

result = 0 # 봉지 수

while n >= 0:
    if n % 5 == 0: # 5로 나눈 나머지가 0인 경우
        result += n // 5 # 5로 나눈 몫 추력
        print(result)
        break
    n -= 3 # 설탕이 5의 배수가 될때까지 반복
    result += 1 # 봉지 추가
else:
    print(-1) # while문이 거짓이 되면 -1 출력


# 10757
import sys
a, b = map(int, sys.stdin.readline().split())
print(a + b)


# 1011


# 1978
n = int(input())
li = list(map(int, input().split()))
answer = 0

for i in li:
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
        if error != 0:
            continue
        else:
            answer += 1
        
print(answer)


# 2581
m = int(input())
n = int(input())

li = []

for i in range(m, n + 1):
    error = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                error += 1
                break
        if error == 0:
            li.append(i)
    
if len(li) > 0:
    print(sum(li))
    print(min(li))
else:
    print(-1)



# 11653
num = int(input())

while num != 1:
    for i in range(2, num + 1):
        if num % i == 0:
            print(i)
            num = num // i
            break


# 1929
import math
import sys
input = sys.stdin.readline

def isPrime(num):
    # 만약 1이라면 소수가 아니므로 false
    if num == 1: return False
    
    # 제곱근까지만 확인
    sq = int(math.sqrt(num))

    for i in range(2, sq + 1):
        # 나눠지면 소수가 아님
        if num % i == 0: return False
    return True


m, n = map(int, input().split())

# m부터 n까지 소수면 소수 출력
for i in range(m, n + 1):
    if isPrime(i):
        print(i)


# 4948
import math

result=[]

def c(a,b):
    cnt=0
    check = [True] * (b+1) 
    
    for i in range(2,int(math.sqrt(b)+1)):
        if check[i] == True:
            for j in range(i*2, b+1, i):
                check[j] = False
    
    for i in range(a+1,b+1): # a보다 크고 b보다 작은 수를 구하기 때문에 3<x<7 x=4,5,6 3개
        if check[i] == True:
            cnt += 1
    return cnt

while True:
    a=int(input())
    if a==0:
        break
    result.append(c(a,2*a))
    
for i in result:
    print(i)