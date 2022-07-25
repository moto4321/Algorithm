# 그림
import sys
sys.setrecursionlimit(10000000)
input = sys.stdin.readline
r, c = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(r)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

lst = []

def dfs(x, y):
    global cnt
    cnt += 1
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < r and ny < c and graph[nx][ny] == 1:
            dfs(nx, ny)

for i in range(r):
    for j in range(c):
        if graph[i][j] == 1:
            cnt = 0
            dfs(i, j)
            lst.append(cnt)

print(len(lst))
print(max(lst))