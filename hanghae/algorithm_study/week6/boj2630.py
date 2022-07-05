n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

blue = 0
white = 0

def solution(x, y, n):
    global white, blue
    color = graph[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if color != graph[i][j]: # 하나라도 같은 색이 아니라면
                solution(x, y, n // 2) # 1사분면
                solution(x, y + n // 2, n // 2) # 2사분면
                solution(x + n // 2, y, n // 2) # 3사분면
                solution(x + n // 2, y + n //2, n // 2) # 4사분면
                return
    if color == 0:
        white += 1
    else:
        blue += 1

solution(0, 0, n)
print(white)
print(blue)