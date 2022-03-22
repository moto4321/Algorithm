# 이진 트리 반전
# leetcode 226

# 파이썬 다운 풀이
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root
        return None


# bfs
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = collections.deque([root])

        while q:
            node = q.popleft()
            # 부모노드로부터 하향식 스왑
            if node:
                node.left, node.right = node.right, node.left

                q.append(node.left)
                q.append(node.right)

        return root