# DFS와 BFS
from collections import deque
n, m, v = map(int, input().split())
graph = [[] for i in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for lst in graph:
    lst.sort()

# for i in range(1, n + 1):
#     graph[i].sort()

visited = [False] * (n + 1)
def dfs(graph, visited, v):
    visited[v] = True
    print(v, end=" ")
    for node in graph[v]:
        if not visited[node]:
            dfs(graph, visited, node)

def bfs(graph, visited, v):
    q = deque([v])
    visited[v] = True
    while q:
        node = q.popleft()
        print(node, end=" ")
        for i in graph[node]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

dfs(graph, visited, v)
visited = [False] * (n + 1)
print()
bfs(graph, visited, v)