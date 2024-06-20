# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = []
        head = res = ListNode(0)
        for listIdx in range(len(lists)):
            if lists[listIdx]:
                pq.append([lists[listIdx].val, listIdx])
                lists[listIdx] = lists[listIdx].next
        heapq.heapify(pq)
        while pq:
            val, listIdx = heapq.heappop(pq)
            res.next = ListNode(val)
            res = res.next
            if lists[listIdx]:
                heapq.heappush(pq, [lists[listIdx].val, listIdx])
                lists[listIdx] = lists[listIdx].next
        return head.next
            
