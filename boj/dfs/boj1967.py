# 트리의 지름

# 메모리 초과
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n + 1)]


def dfs(x, wei):
    for i in graph[x]:
        a, b = i
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, wei + b)


# 트리 구현
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

# 1번 노드에서 가장 먼 곳을 찾는다.
distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)

# 위에서 찾은 노드에 대한 가장 먼 노드를 찾는다.
start = distance.index(max(distance))
distance = [-1] * (n + 1)
distance[start] = 0
dfs(start, 0)

print(max(distance))



# 정답
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(num):
    global answer
    if graph[num]:
        left, right = 0,0
        for i, d in graph[num]:
            now_distance = dfs(i) + d
            if now_distance > right:
                left, right = right, now_distance
            elif now_distance > left:
                left = now_distance
        answer = max(answer, left+right)
        return right
    else:
        return 0

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y, c = map(int, input().split())
    graph[x].append((y,c))

answer = 0
dfs(1)
print(answer)