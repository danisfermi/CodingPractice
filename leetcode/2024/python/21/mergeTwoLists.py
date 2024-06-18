# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = res = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                res.next = list1
                list1 = list1.next
            else:
                res.next = list2
                list2 = list2.next
            res = res.next
        while list1:
            res.next = list1
            list1 = list1.next
            res = res.next
        while list2:
            res.next = list2
            list2 = list2.next
            res = res.next
        return head.next
