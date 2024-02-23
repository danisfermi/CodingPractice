class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        sPtr = fPtr = head
        if fPtr == None or fPtr.next == None:
            return None
        while fPtr and fPtr.next:
            sPtr = sPtr.next
            fPtr = fPtr.next.next
            if sPtr == fPtr:
                break
        if sPtr != fPtr:
            return None
        sPtr = head
        while sPtr != fPtr:
            sPtr = sPtr.next
            fPtr = fPtr.next
        return sPtr
