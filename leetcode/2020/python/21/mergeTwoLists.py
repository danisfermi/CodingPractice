class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        temp = l3 = ListNode(0)
        while l1 and l2:
            l3.next = ListNode(min(l1.val if l1 else 101, l2.val if l2 else 101))
            l3 = l3.next
            if l1 and l3.val == l1.val:
                l1 = l1.next
            elif l2 and l3.val == l2.val:
                l2 = l2.next
        while l1:
            l3.next = ListNode(l1.val)
            l1 = l1.next
            l3 = l3.next
        while l2:
            l3.next = ListNode(l2.val)
            l2 = l2.next
            l3 = l3.next
        return temp.next
