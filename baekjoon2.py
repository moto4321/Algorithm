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


# 2839
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