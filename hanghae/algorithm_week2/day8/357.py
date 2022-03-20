# 일정 재구성
# leetcode 332

# dfs 풀이
import collections

graph = collections.defaultdict(list)

tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]

# 그래프 순서대로 구성
for a, b in sorted(tickets):
    graph[a].append(b)

route = []

def dfs(a):
    # 첫 번째 값을 읽어 어휘 순 방문
    while graph[a]:
        dfs(graph[a].pop(0))
    route.append(a)


dfs('JFK')
# return route[::-1]
print(route)