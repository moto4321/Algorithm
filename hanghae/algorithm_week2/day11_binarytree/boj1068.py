# 트리

# 내 풀이(실패)
from collections import defaultdict

n = int(input())
graph = defaultdict(list)

for i in range(n):
    graph[i].append(int(input()))

m = int(input())

# 해당 노드 삭제
graph.remove(m)
# 해당 노드를 부모로 가지는 자식노드 삭제
for i in graph:
    if m in graph[i]:
        graph.remove(i)

print(len(graph))


# 정답 풀이
n = int(input())  # 5
# 각 노드의 부모를 parents에 저장한다.
parents = list(map(int, input().split()))  # -1 0 0 1 1
del_node = int(input())  # 2
# tree맵
tree = {}

# parents를 for문으로 돌면서 삭제할 노드이거나 삭제할 노드를 부모로 둔 노드를 제외하고 tree 에 저장한다.
for i in range(n): # n = 5
    if i == del_node or parents[i] == del_node:
        continue
    if parents[i] in tree:
        tree[parents[i]].append(i)
    else:
        tree[parents[i]] = [i]

# 삭제한 노드가 루트라면 빈 리스트를, 아니라면 [-1]를 que에 저장한다.
res = 0
if -1 in tree:
    que = [-1]
else:
    que = []

# 트리를 돌면서 리프 노드의 개수를 센다.
while que:
    node = que.pop()
    if node not in tree:
        res += 1
    else:
        que += tree[node]

print(res)