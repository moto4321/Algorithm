# 전보

import heapq

n, m, c = map(int, input().split())
INF = int(1e9)
# graph = [[INF] * (n + 1) for _ in range(n + 1)]
# for _ in range(m):
#     x, y, z = map(int, input().split())
#     graph[x][y] = z
#
# for i in range(1, n + 1):
#     graph[i][i] = 0
#


graph = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

q = []
dist = [INF] * (n + 1)
heapq.heappush(q, (c, 0))
dist[c] = 0

while q:
    cur, fee = heapq.heappop(q)

    if dist[cur] < fee:
        continue

    for node, i in graph[cur]:
        cost = fee + i
        if cost < dist[node]:
            dist[node] = cost
            heapq.heappush(q, (node, cost))

cities = 0
for i in range(1, len(dist)):
    if dist[i] != INF and dist[i] != 0:
        cities += 1

print(cities, max(dist[1:]))
