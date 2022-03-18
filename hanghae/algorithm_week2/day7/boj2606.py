



n = int(input())
m = int(input())

graph = [0] * (m + 1)

for i in range(1, m + 1):
    graph[i] = list(map(int, input().split()))

