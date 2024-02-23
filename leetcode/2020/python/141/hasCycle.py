class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        sPtr = fPtr = head
        if fPtr is None or fPtr.next is None:
            return False
        while fPtr and fPtr.next:
            sPtr = sPtr.next
            fPtr = fPtr.next.next
            if fPtr == sPtr:
                return True
        return False
