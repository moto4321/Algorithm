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