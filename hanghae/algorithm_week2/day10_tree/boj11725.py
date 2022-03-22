# 트리의 부모 찾기
# leetcode 11725

from collections import deque

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

n = int(input())

lst = []
for _ in range(n - 1):
    a, b = map(int, input().split())
    lst.append((a, b))




q = deque([1])

while q:
    cur = q.popleft()
... 안떠오름



# 정답
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input())
tree = [[] for _ in range(n + 1)]
parents = [-1] * (n + 1)
# 트리 구조 입력
for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)


def dfs(n):
    # 연결된 노드들부터 parents[i]의 부모가 없으면 부모 설정 해주고, dfs돌린다.
    for i in tree[n]:
        if parents[i] == -1:
            parents[i] = n
            dfs(i)


dfs(1)
for i in range(2, n + 1):
    print(parents[i])

##
