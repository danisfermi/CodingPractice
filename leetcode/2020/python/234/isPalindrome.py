class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        temp = head
        fptr = sptr = head
        # Find mid
        while fptr and fptr.next:
            fptr = fptr.next.next
            prev_sptr = sptr
            sptr = sptr.next
        if fptr != None:
            mid = sptr
            sptr = sptr.next
        prev_sptr = None
        # Reverse
        prev = None
        while sptr:
            nex = sptr.next
            sptr.next = prev
            prev = sptr
            sptr = nex
        sptr = prev
        # Compare
        while sptr and temp:
            if sptr.val != temp.val:
                return False
            sptr = sptr.next
            temp = temp.next
        return True
