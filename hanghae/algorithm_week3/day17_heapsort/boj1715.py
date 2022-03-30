# 카드 정렬하기

import heapq
n = int(input())
lst = []
for _ in range(n):
    heapq.heappush(lst, int(input()))

answer = 0

while len(lst) > 1:
    first = heapq.heappop(lst)
    second = heapq.heappop(lst)
    answer += first + second
    heapq.heappush(lst, first + second)
print(answer)