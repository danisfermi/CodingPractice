class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = prev = ListNode(0)
        prev.next = head
        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next
            prev.next = b
            a.next = b.next
            b.next = a
            prev = prev.next.next
        return temp.next
