#Given a Linked List and a number n, write a function that returns the value at the n’th node from the end of the #Linked List.
#1->2->3->4->5

'''
n = 0
n=2
output: 4
'''

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

'''
Time Complexity = O(n)
Space Complexity = O(1)
'''

def helper(head, n):
    slow = fast = head
    # Set fast pointer to be n + head
    while n:
        if fast:
            fast = fast.next
        else:
            return -1
        n -= 1
    # Traverse both to see if fast reaches end
    while fast:
        fast = fast.next
        slow = slow.next
    return slow.val
