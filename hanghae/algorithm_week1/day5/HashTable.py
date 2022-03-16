class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

from collections import defaultdict

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = defaultdict(ListNode)

    def put(self, key: int, value: int):
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key: int):
        index = key % self.size
        # 노드가 존재하지 않는 경우
        if self.table[index].value is None:
            return -1

        # 노드가 존재하는 경우
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key: int):
        index = key % self.size
        if self.table[index].value is None:
            return

        # 인덱스가 첫 번째 노드일 때 삭제 처리
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return

        # 연결 리스트 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev = p
            p = p.next



from hashtable.structures import MyHashTable


def test_hashtable():
    ht = MyHashTable()

    ht.put(1, 1)
    ht.put(2, 2)
    assert ht.get(1) == 1
    assert ht.get(3) == -1

    ht.put(2, 1)
    assert ht.get(2) == 1

    ht.remove(2)
    assert ht.get(2) == -1


def test_birthday_problem():
    import random
    TRIALS = 100000
    same_birthdays = 0

    for _ in range(TRIALS):
        birthdays = []
        for i in range(23):
            birthday = random.randint(1, 365)
            if birthday in birthdays:
                same_birthdays += 1
                break
            birthdays.append(birthday)

    print(f"{same_birthdays / TRIALS * 100}%")


if __name__ == "__main__":
    test_birthday_problem()
    test_hashtable()