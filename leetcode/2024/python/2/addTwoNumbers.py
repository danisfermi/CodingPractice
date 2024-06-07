# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = temp = ListNode(0)
        carry = 0
        sum = 0
        while l1 or l2 or carry:
            a = l1.val if l1 else 0
            b = l2.val if l2 else 0
            sum = a + b + carry
            carry = sum//10
            sum = sum%10
            res.next = ListNode(sum)
            res = res.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return temp.next
