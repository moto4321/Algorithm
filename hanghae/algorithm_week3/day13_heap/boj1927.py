# 최소 힙
import heapq
import sys

input = sys.stdin.readline
n = int(input())

cal = []
for _ in range(n):
    cal.append(int(input()))

result = []

for num in cal:
    if num == 0:
        if not result:
            print(0)
            continue
        print(heapq.heappop(result))
    else:
        heapq.heappush(result, num)


# 좀 더 코드를 줄여본 풀이

import heapq

n = int(input())

result = []

for _ in range(n):
    x = int(input())
    if x == 0:
        if not result:
            print(0)
        else:
            print(heapq.heappop(result))
    else:
        heapq.heappush(result, x)
