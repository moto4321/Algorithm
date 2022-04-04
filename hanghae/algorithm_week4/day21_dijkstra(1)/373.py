# leetcode 743

# arrived라는 변수에 dictionary형으로 만들어 저장
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for _from, _to, time in times:
            graph[_from].append((_to, time))

        arrived = defaultdict(int)
        q = [(0, k)]

        while q:
            time, node = heapq.heappop(q)
            if node not in arrived:
                arrived[node] = time
                for _next, delay in graph[node]:
                    arrive_time = time + delay
                    heapq.heappush(q, (arrive_time, _next))

        if len(arrived.keys()) == n:
            return max(arrived.values())

        return -1


# dist 변수에 거리 저장
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        INF = int(1e9)
        distance = [INF] * (n + 1)

        for (a, b, c) in times:
            graph[a].append((b, c))

        q = []
        heapq.heappush(q, (0, k))
        distance[k] = 0

        while q:
            dist, cur = heapq.heappop(q)

            if distance[cur] < dist:
                continue

            for node, node_dist in graph[cur]:
                cost = dist + node_dist
                if cost < distance[node]:
                    distance[node] = cost
                    heapq.heappush(q, (cost, node))

        answer = max(distance[1:])

        if answer == INF:
            return -1
        return answer