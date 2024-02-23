class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        temp = head
        res = 0
        while temp:
            res = (res << 1) | temp.val
            temp = temp.next
        return res
