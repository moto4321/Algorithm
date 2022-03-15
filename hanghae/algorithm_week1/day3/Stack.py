# 스택과 큐 직접 구현해보기

class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    # push, pop, is_empty
    def is_empty(self):
        return self.top is None

    def push(self, val):
        self.top = Node(val, self.top)
        # Node 속 self.top 은 기존 탑이 다음 대상이 된다는 뜻

    def pop(self):
        if not self.top:
            return None

        node = self.top
        self.top = self.top.next # 기존의 탑을 바로 아래녀석으로 지정하자

        return node.item


# 파이썬에서는 스택을 쓸때 사실은 리스트로 쓰면된다!!!