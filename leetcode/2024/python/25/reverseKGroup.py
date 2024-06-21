# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummyNode = ListNode(0, head)
        groupPrev = dummyNode
        while True:
            kth = self.getKth(groupPrev, k)
            if kth is None:
                break
            groupNext = kth.next
            prev = kth.next
            curr = groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummyNode.next
            
    def getKth(self, node, k):
        while node and k:
            node = node.next
            k -= 1
        return node
