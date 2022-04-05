# 정확한 순위

with open('testcase_rank.txt') as f:
    print("*" * 80, f.name)
    INF = int(1e9)
    sys.stdin = f
    input = sys.stdin.readline

    N, M = map(int, input().split())
    dist = [[INF] * (N + 1) for _ in range(N + 1)]

    for idx in range(1, N + 1):
        dist[idx][idx] = 0

    for _ in range(M):
        a, b = map(int, input().split())
        dist[a][b] = 1

    for k in range(1, N + 1):
        for a in range(1, N + 1):
            for b in range(1, N + 1):
                dist[a][b] = min(dist[a][b], dist[a][k] + dist[k][b])

    result = 0
    for cur in range(1, N + 1):
        cnt = 0
        # 현재 노드(cur)를 기준으로,
        # 다른 노드(node)로 갈 방법이 있는지 센다.
        for node in range(1, N + 1):
            if dist[cur][node] != INF or dist[node][cur] != INF:
                cnt += 1
        # 모든 노드에 대해 갈 수 있다면 순위를 아는 것.
        if cnt == N:
            result += 1
    print(result)