# 녹색 옷 입은 애가 젤다지?

import heapq

num = 0
while True:
    n = int(input())
    if n == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(n)]
    INF = int(1e9)
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = 0
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]

    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    while q:
        cur, row, col = heapq.heappop(q)

        # if cur < graph[row][col]:
        #     continue

        if row == n - 1 and col == n - 1:
            num += 1
            print(f'Problem {num}: {distance[n - 1][n - 1]}')
            break

        for i in range(4):
            nr = row + dr[i]
            nc = col + dc[i]
            if 0 <= nr < n and 0 <= nc < n:
                cost = cur + graph[nr][nc]
                if cost < distance[nr][nc]:
                    distance[nr][nc] = cost
                    # heapq.heappush(q, (distance[nr][nc], nr, nc))
                    heapq.heappush(q, (cost, nr, nc))