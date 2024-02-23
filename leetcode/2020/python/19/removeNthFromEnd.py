class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow = head
        fast, f = head, 1
        while f <= n:
            fast, f = fast.next, f+1  
        while fast and fast.next:
            slow = slow.next
            fast = fast.next  
        if not fast:
            return slow.next
        if slow.next == fast:
            slow.next = None
            return head
        slow.next = slow.next.next
        return head
