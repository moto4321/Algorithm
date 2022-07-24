# 치즈
from collections import deque

r, c = map(int, input().split()) # 세로 가로
board = [list(map(int, input().split())) for _ in range(r)]
cheese = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def find_air():
    visited = [[False] * c for _ in range(r)]

    q = deque()
    q.append([0, 0])
    visited[0][0] = True
    cnt = 0
    while q:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < r and 0 <= nx < c and not visited[ny][nx]:
                if board[ny][nx] == 0:
                    visited[ny][nx] = True
                    q.append([ny, nx])
                elif board[ny][nx] == 1:
                    board[ny][nx] = 0
                    cnt += 1
                    visited[ny][nx] = True
    cheese.append(cnt)
    return cnt



time = 0
while True:
    time += 1
    cnt = find_air()
    if cnt == 0:
        break

print(time - 1)
print(cheese[-2])



####

import collections

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

def bfs():
    queue = collections.deque()
    queue.append((0,0))
    check = [[False] * m for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    count = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and check[nx][ny] == False:
                    check[nx][ny] = True
                    queue.append((nx,ny))
                # (0,0) 에서 시작해서 처음 만나는 1들은 모두 가장자리이다.
                elif graph[nx][ny] == 1:
                    # queue에 추가해주는게 아니라 0으로 바꿔줘 녹게만들어준다.
                    graph[nx][ny] = 0
                    count += 1
                    check[nx][ny] = True
    return count

result = []
time = 0
while True:
    count = bfs()
    result.append(count)
    # count가 0이면 모든 치즈가 녹았다는 소리이다.
    if count == 0:
        break
    time += 1

print(time)
# 한시간 전에(모두 녹기전 단계) count를 출력해야 되므로 [-2]를 출력한다.
print(result[-2])