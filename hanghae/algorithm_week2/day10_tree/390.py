# 이진 트리 직경
# leetcode 104

# 아래와 같이 외쪽 길이 오른쪽 길이를 구하고 합치려는 아이디어였지만 풀리지 않았다.
depth_left = 0
depth_right = 0

if root is None:
    return 0

left = root.left
right = root.right

q1 = deque([left])
q2 = deque([right])


def dep_left():
    while q1:
        nonlocal depth_left
        depth_left += 1
        for _ in range(len(q1)):
            cur = q1.popleft()
            if cur.left:
                q1.append(cur.left)
            if cur.right:
                q1.append(cur.right)
    return depth_left


def dep_right():
    while q2:
        nonlocal depth_right
        depth_right += 1
        for _ in range(len(q2)):
            cur = q2.popleft()
            if cur.left:
                q2.append(cur.left)
            if cur.right:
                q2.append(cur.right)

    return depth_right

return dep_left() + dep_right()


# 다음은 책에서 소개하는 풀이
longest: int = 0

def diameterOfBinaryTree(self, root: TreeNode) -> int:
    def dfs(node: TreeNode) -> int:
        if not node:
            return -1

        # 왼쪽, 오른쪽의 각 리프 노드까지 탐색
        left = dfs(node.left)
        right = dfs(node.right)

        # 가장 긴 경로
        self.longest = max(self.longest, left + right + 2)
        # 상태값
        return max(left, right) + 1

    dfs(root)
return self.longest