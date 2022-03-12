class Person:
    def __init__(self, name):
        self.name = name

    def sayhello(self, to):
        print(f"hello {to}, I'm {self.name}")


rtan = Person("rtanny")
rtan.sayhello("wooseok")

# ====================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 삽입, 삭제 등이 있지만 여기서는 삽입 기능만 구현
class LinkedList:
    def __init__(self):
        self.head = None
        # self.head = ListNode(val)

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head
        while node.next:
            node = node.next
        node.next = ListNode(val, None)

    def delete(self, val):
        node = self.head # head 노드의 복삿값
        if node.val == val: # head 노드가 제거될 값과 같을 경우
            self.head = node.next
            del node
            # head노드를 head노드의 다음 노드로 지정하고 삭제
            return

        while not node:
            # node의 값과 제거될 키값이 같은 경우 중지
            if node.val == val:
                break
            prev = node
            node = node.next
        if not node: # node가 None이면 종료
            return
        prev.next = node.next # node노드 이전 노드가 node노드의 다음 노드를 가리킴
        # 그렇게 해야 연결이 중간에 있는 노드가 빠져도 연결이 되기 때문
        del node
        return



# LinkedList test
lst = [1, 2, 3]
l1 = LinkedList()
for e in lst:
    l1.append(e)

print(l1)