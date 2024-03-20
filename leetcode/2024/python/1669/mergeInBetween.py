# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = ListNode()
        end = list1

        # Set start to node a - 1 and end to node b
        for index in range (b):
            if index == a - 1:
                start = end
            end = end.next

        # Connect the start node to list2
        start.next = list2

        # Find the tail of list2
        while (list2.next is not None):
            list2 = list2.next
            
        # Set the tail of list2 to end.next
        list2.next = end.next
        end.next = None
        
        return list1
