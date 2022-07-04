# 바이러스
# 컴퓨터수
n = int(input())
# 컴퓨터 쌍의 수(간선)
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)

def dfs(graph, visited, v):
    visited[v] = True
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, visited, i)

dfs(graph, visited, 1)
print(sum(visited) - 1)