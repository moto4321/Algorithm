# 최단경로

# 내 풀이
import heapq

v, e = map(int, input().split()) # 정점 v 간선 e
k = int(input())
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

INF = int(1e9)
dist = [INF] * (v + 1)

q = []
heapq.heappush(q, (0, k))
dist[k] = 0
while q:
    c, cur = heapq.heappop(q)

    if dist[cur] < c:
        continue

    for node, i in graph[cur]:
        cost = dist[cur] + i
        if cost < dist[node]:
            dist[node] = cost
            heapq.heappush(q, (cost, node))

for i in range(1, len(dist)):
    if dist[i] != INF:
        print(dist[i])
    else:
        print('INF')