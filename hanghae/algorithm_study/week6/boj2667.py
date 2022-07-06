# 단지번호붙이기
n = int(input())
graph = [list(map(int, input())) for _ in range(n)]
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

danji_tot = 0
danji_each = 0
danji_cnt = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global danji_cnt, danji_each, danji_tot
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0 and nx < n and ny < n and graph[nx][ny] == 1:
            danji_each += 1
            graph[nx][ny] = 0
            dfs(nx, ny)



for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            danji_tot += 1
            danji_each += 1
            graph[i][j] = 0
            dfs(i, j)
            danji_cnt.append(danji_each)
            danji_each = 0


print(danji_tot)
danji_cnt.sort()
for num in danji_cnt:
    print(num)

# 근데 내가 예전에 푼게 속도가 더 빠르네...
