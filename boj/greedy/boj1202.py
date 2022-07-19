# 보석 도둑
import heapq
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
# 2, 1

jewel_list = [list(map(int, input().split())) for _ in range(n)]
# [5, 10], [100, 100]
bag_list = [int(input()) for _ in range(k)]
# 11
jewel_list.sort() # [[5, 10], [100, 100]]
bag_list.sort() # [11]

result = 0
temp = []

for bag_weight in bag_list:
    while jewel_list and bag_weight >= jewel_list[0][0]:
        heapq.heappush(temp, -jewel_list[0][1]) # Max heap
        heapq.heappop(jewel_list)
    if temp:
        result += heapq.heappop(temp)
    elif not jewel_list:
        break

print(-result)