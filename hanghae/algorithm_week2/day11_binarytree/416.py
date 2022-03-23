# 최소 높이 트리
# leetcode 310

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)

        if n <= 1:
            return [0]

        # 양방향 그래프 구성
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        # 첫 번째 리프 노드 추가
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)

        # 루트 노드만 남을 때까지 제거
        while n > 2:
            n -= len(leaves)  # n = 10  # len(leaves) = 5
            new_leaves = []
            for leaf in leaves:  # [1, 2, 10, 7, 9]
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)

            leaves = new_leaves

        return leaves



