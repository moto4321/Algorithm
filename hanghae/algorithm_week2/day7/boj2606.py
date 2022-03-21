# 바이러스

# bfs
from collections import deque

n = int(input())
m = int(input())
graph = [[] * i for i in range(n + 1)]
for i in range(1, m + 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
visited[1] = True
q = deque([1])
count = 0
while q:
    v = q.popleft()
    count += 1
    for each in graph[v]:
        if visited[each] == False:
            q.append(each)
            visited[each] = True

print(count - 1)


# dfs 방식

n = int(input())
m = int(input())
graph = []
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)


# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for


def dfs():






















