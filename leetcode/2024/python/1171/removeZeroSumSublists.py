# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0)
        front.next = head
        m = {}
        m[0] = front
        prefix = 0
        curr = front
        while curr:
            prefix += curr.val
            m[prefix] = curr
            curr = curr.next
        prefix = 0
        curr = front
        while curr:
            prefix += curr.val
            curr.next = m[prefix].next
            curr = curr.next
        return front.next
