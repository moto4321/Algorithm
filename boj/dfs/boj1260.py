# DFS와 BFS
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for lst in graph:
    lst.sort()

visited = [False] * (n + 1)
dfs_lst = []
bfs_lst = []
def dfs(start, visited, graph):
    dfs_lst.append(start)
    visited[start] = True
    for node in graph[start]:
        if visited[node] == False:
            dfs(node, visited, graph)

def bfs(start, visited, graph):
    q = deque([start])
    visited[start] = True
    while q:
        node = q.popleft()
        bfs_lst.append(node)
        for num in graph[node]:
            if visited[num] == False:
                q.append(num)
                visited[num] = True


dfs(v, visited, graph)
visited = [False] * (n + 1)
bfs(v, visited, graph)

print(*dfs_lst)
print(*bfs_lst)