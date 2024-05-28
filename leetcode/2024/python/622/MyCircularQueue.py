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
