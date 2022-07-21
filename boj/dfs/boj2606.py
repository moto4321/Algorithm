# 바이러스
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


visited = [False] * (n + 1)
result = []
def dfs(start, visited, graph):
    visited[start] = True
    result.append(start)
    for node in graph[start]:
        if not visited[node]:
            dfs(node, visited, graph)

dfs(1, visited, graph)

print(len(result) - 1)