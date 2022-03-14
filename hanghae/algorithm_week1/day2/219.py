# leetcode 206

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 재귀 함수를 이용한 방법
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next = node.next
            node.next = prev

            return reverse(next, node)

        return reverse(head)

        # 반복문을 이용한 방법
        node, prev = head, None

        while node:
            next = node.next
            node.next = prev  # prev를 가리킴
            prev = node
            node = next
        return prev