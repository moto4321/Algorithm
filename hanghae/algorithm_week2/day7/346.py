# 조합
# leetcode 77

# 내 풀이
class Solution:
    from itertools import combinations

    def combine(self, n: int, k: int) -> List[List[int]]:
        lst = [i for i in range(1, n + 1)]

        return combinations(lst, k)


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []

        def dfs(elements, start: int, k: int):
            if k == 0:
                results.append(elements[:])
                return

            # 자신 이전의 모든 값을 고정하여 재귀 호출
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()

        dfs([], 1, k)
        return results
