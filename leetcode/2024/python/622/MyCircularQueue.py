class ListNode():
    def __init__(self,val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.left = ListNode(0, None, None)
        self.right = ListNode(0, self.left, None)
        self.left.next = self.right

    def enQueue(self, value: int) -> bool:
        if self.isFull(): 
            return False
        else:
            curr = ListNode(value, self.right.prev, self.right)
            self.right.prev.next = curr
            self.right.prev = curr
            self.k -= 1
            return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        else:
            self.left.next = self.left.next.next
            self.left.next.prev = self.left
            self.k += 1
            return True
        
    def Front(self) -> int:
        return -1 if self.isEmpty() else self.left.next.val

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.right.prev.val

    def isEmpty(self) -> bool:
        return self.left.next == self.right

    def isFull(self) -> bool:
        return self.k == 0

'''
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.q = [0]*k
        self.front= self.rear = -1

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.size
        self.q[self.rear] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        item = self.q[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        if self.front == -1:
            return -1
        return self.q[self.front]

    def Rear(self) -> int:
        if self.rear == -1:
            return -1
        return self.q[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1

    def isFull(self) -> bool:
        if self.rear == (self.front - 1) % (self.size):
            return True
        return False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
'''
