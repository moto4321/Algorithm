# leetcode 787

# queue로 풀이
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        #make an adjaceny matrix
        #this will follow modified dijkatra's algo
        graph = [[] for i in range(n)]
        for u, v, w in flights:
            graph[u].append((v, w))
        #initialize infinite values for all nodes
        output = [float('inf') for i in range(n)]
        #start with source and hence mark it's weight as 0
        output[src] = 0
        #construct graph
        Q = deque()
        #append the src , -1 as strp and 0 as cost to graph
        Q.append((src, -1, 0))
        #now iterate over graph
        while Q:
            u, step, cost = Q.popleft()
            #if i have exhausted all steps
            if step >= k:
                continue
            for v, w in graph[u]:
                #classic dijkatr's algo
                if cost + w < output[v]:
                    output[v] = cost + w
                    Q.append((v, step + 1, cost + w))
        if output[dst] == float('inf'):
            return -1
        return output[dst]


# heapq로 풀이
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append([v, w])
        k = 0
        visit = {}
        Q = [(0, src, 0)]
        while Q:
            price, node, k = heapq.heappop(Q)
            if node == dst:
                return price
            if node not in visit or visit[node] > k:
                visit[node] = k
                for v, w in graph[node]:
                    if k <= K:
                        alt = price + w
                        heapq.heappush(Q, (alt, v, k + 1))
        return -1