# 운동

v, e = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (v + 1) for _ in range(v + 1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

# for i in range(1, v + 1):
#     graph[i][i] = 0
# 이게 포인트

for k in range(1, v + 1):
    for x in range(1, v + 1):
        for y in range(1, v + 1):
            graph[x][y] = min(graph[x][y], graph[x][k] + graph[k][y])

result = INF

for i in range(1, v + 1):
    result = min(result, graph[i][i])

if result == INF:
    print(-1)
else:
    print(result)