# structures.py
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# prac.py
# from binarytree.structures import TreeNode

def make_tree_by(lst, idx):
    parent = None
    if idx < len(lst):
        value = lst[idx]
        if value is None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(lst, 2 * idx + 1)
        parent.right = make_tree_by(lst, 2 * idx + 2)

    return parent


# 이진 트리의 최대 깊이
# test_max_depth.py
from collections import deque

# from binarytree.prac import make_tree_by

def test_max_depth(lst):
    root = make_tree_by(lst, 0)
    if not root:
        return 0

    q = deque([root])
    depth = 0

    while q:
        depth += 1
        for _ in range(len(q)):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    return depth


assert test_max_depth(lst=[]) == 0
assert test_max_depth(lst=[3, 9, 20, None, None, 15, 7]) == 3