# 가장 긴 동일 값의 경로
# leetcode 687
class Solution:

    def longestUnivaluePath(self, root: TreeNode) -> int:
        result: int = 0

        def dfs(node: TreeNode):
            nonlocal result

            if node is None:
                return 0

            # 존재하지 않는 노드까지 DFS 재귀 탐색
            left = dfs(node.left)
            right = dfs(node.right)

            # 현재 노드가 자식와 동일한 경우 거리 1 증가
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0

            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            # 왼쪽과 오른쪽 자식 노드 간 거리의 합 최대값이 결과
            result = max(result, left + right)
            # 자식 노드 상태값 중 큰 값 리턴
            return max(left, right)

        dfs(root)
        return result