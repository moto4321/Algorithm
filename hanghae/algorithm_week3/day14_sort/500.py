# 삽입 정렬 리스트
# leetcode 147
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next

            cur.next, head.next, head = head, cur.next, head.next

            if head and cur.val > head.val:
                cur = parent # 다시 cur를 맨 앞으로 이동

        return parent.next

# 또 다른 풀이
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy_head = ListNode()
        curr = head

        # curr가 존재하는 동안 반복
        while curr:
            prev_pointer = dummy_head
            next_pointer = dummy_head.next

            # next_pointer가 있는 경우
            while next_pointer:
                # 현재의 값보다 다음노드 값이 더 크다면 정렬을 만족하므로 break
                if curr.val < next_pointer.val:
                    break
                # 만족을 안한다면 비교를 위해 다음으로 이동
                prev_pointer = prev_pointer.next
                next_pointer = next_pointer.next

            # 정렬 되기 전의 다음 값으로 연결하기 위해 임시 변수 temp를 만든다.
            temp = curr.next

            curr.next = next_pointer
            prev_pointer.next = curr

            curr = temp

        # 맨 처음 아무것도 없는 값을 dummy_head로 설정했기 때문에 그 다음값을 리턴해야 한다.
        return dummy_head.next