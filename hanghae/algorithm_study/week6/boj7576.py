n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.append(list(map(int, input().split())))

# 북, 동, 남, 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def grow_tomato(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < m and ny < n and nx >= 0 and ny >= 0 and graph[nx][ny] != -1:
            graph[nx][ny] = 1


day = 0
flag = False
for i in range(m):
    for j in range(n):
        day += 1
        if graph[i][j] == 1:
            grow_tomato(i, j)
        if graph.count(0) == 0:
            flag = True
            print(day)
            break

if flag == False:
    print(-1)


# 정답 풀이
from collections import deque
m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
q = deque([])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 정답이 담길 변수
res = 0

# q에 처음 받은 토마토의 위치 좌표를 append
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            q.append([i, j])

def bfs():
    while q:
        x, y = q.popleft()
        # 처음 토마토 사분면의 익힐 토마토들을 찾아본다.
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and ny >= 0 and nx < n and ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append([nx, ny])

bfs()
for i in graph:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res - 1)