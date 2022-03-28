# 리스트 정렬
# leetcode

# 리스트 정렬
# leetcode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        while head != None:
            lst.append(head.val)
            head = head.next

        lst.sort()

        newList = ListNode(0)

        result = newList

        for num in lst:
            newList.next = ListNode(num)
            newList = newList.next

        return result.next