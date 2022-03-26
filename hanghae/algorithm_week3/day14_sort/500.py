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

        while curr:
            prev_pointer = dummy_head
            next_pointer = dummy_head.next

            while next_pointer:
                if curr.val < next_pointer.val:
                    break
                prev_pointer = prev_pointer.next
                next_pointer = next_pointer.next

            temp = curr.next

            curr.next = next_pointer
            prev_pointer.next = curr

            curr = temp

        return dummy_head.next