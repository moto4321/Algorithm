# 최대 힙
import heapq
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
        print(-heapq.heappop(result))
    else:
        heapq.heappush(result, -num)




# 최대 힙
import heapq
import sys
input = sys.stdin.readline
n = int(input())

result = []
for _ in range(n):
    num = (int(input()))
    if num == 0:
        if not result:
            print(0)
            continue
        print(-heapq.heappop(result))
    else:
        heapq.heappush(result, -num)


