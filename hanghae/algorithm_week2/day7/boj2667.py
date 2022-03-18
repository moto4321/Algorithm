# 단지 번호 붙이기


# 내 풀이 (스택이용 근데 틀림)
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(graph)

danji_list = []
stack = []
danji_cnt = 0
for row in range(n):
    for col in range(n):
        if graph[row][col] != '1':
            continue

        danji_cnt += 1
        danji_result = 0
        stack = [(row, col)]
        while stack:
            x, y = stack.pop()
            graph[x][y] = '0'
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= n or ny >= n or graph[nx][ny] == '0':
                    continue
                stack.append((nx, ny))
                danji_result += 1
        danji_list.append(danji_result)

print(danji_cnt) # 단지 수
for cnt in danji_list:
    print(cnt)


# 재귀함수를 이용한 풀이
n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

print(graph)

def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False


count = 0
result = 0

for i in range(n):
    for j in range(n):
        if DFS(i, j) == True:
            num.append(count)
            result += 1
            count = 0

num.sort()
print(result)
for i in range(len(num)):
    print(num[i])