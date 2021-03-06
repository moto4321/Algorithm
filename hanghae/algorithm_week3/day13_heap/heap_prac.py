class BinaryMaxHeap:
    def __init__(self):
        # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용한다.
        self.items = [None]

    def __len__(self):
        # len() 연산을 가능하게 하는 매직 메서드 덮어쓰기(Override).
        return len(self.items) - 1

    def _percolate_up(self):
        # percolate: 스며들다.
        cur = len(self)
        # left 라면 2*cur, right 라면 2*cur + 1 이므로 parent 는 항상 cur // 2
        parent = cur // 2

        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        biggest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right
        # 위 두 if문이 끝나고 나면 부모, 왼쪽, 오른쪽 값 중 가장 큰 값이 저장되어있을 것이다.

        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self._percolate_down(biggest)

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root


######################################################################

import heapq

# from heap.structures import BinaryMaxHeap


def test_maxheap_we_made(lst, k):
    maxheap = BinaryMaxHeap()

    # for 문을 눈여겨봐두세요.
    # 힙정렬 시간복잡도 계산의 토대입니다.
    for elem in lst:
        maxheap.insert(elem)

    return [maxheap.extract() for _ in range(k)][k - 1]


def test_maxheap_heapq(lst, k):
    return heapq.nlargest(k, lst)[-1]


assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 2) == 5
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 3) == 5
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 5) == 3
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 6) == 3
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 7) == 2
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 8) == 2
assert test_maxheap_we_made([3, 2, 3, 1, 2, 4, 5, 5, 6], 9) == 1


assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 1) == 6
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 2) == 5
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 3) == 5
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 5) == 3
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 6) == 3
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 7) == 2
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 8) == 2
assert test_maxheap_heapq([3, 2, 3, 1, 2, 4, 5, 5, 6], 9) == 1