# 유기농 배추
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
t = int(input())

for _ in range(t):
    count = 0
    # 가로길이, 세로길이, 배추 개수
    m, n, k = map(int, input().split())
    graph = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
        
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    def dfs(x, y):
        if x < 0 or y < 0 or x >= m or y >= n or graph[x][y] == 0:
            return
            
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                count += 1
                dfs(i, j)
    
    print(count)

