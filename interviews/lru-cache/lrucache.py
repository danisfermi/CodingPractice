'''
LRU Cache
1. Insert a key - value
2. Retrieve a value, given a key

limit - total size
hash map/dict - key: node(value)
'''

# Linked List Node
class Node:
	def __init__(self, key, value, prev = None, next = None):
		self.key = key
		self.val = value
		self.prev = prev
		self.next = next
# head -> tail
class LRU:
	def __init__(self, k):
		self.limit = k
		self.curr = 0
		self.map = {}
		self.head = None
		self.tail = None
	
	# delete a node
	def deleteNode(self, node):
		if self.tail == node:
			self.tail = node.prev
		if node != self.head:
			prev = node.prev
		next = node.next
		prev.next = next
		if next:
			next.prev = prev
		del node

	# add a node - always at beginning
	def addNode(self, node):
		if self.head:
			node.next = self.head
			self.head.prev = node
		else:
			self.tail = node
		self.head = node

	def printNodes(self):
		temp = self.head
		print(self.head.key, " ", self.tail.key)
		while temp:
			print(temp.key, ",", temp.val, "->", )
			temp = temp.next

	def insert(self, key, value):
		print("Inserting ", key, " ", value)
		# if key already present - retrieve node, delete and add at beginning
		if key in self.map:
			node = self.map[key]
			self.deleteNode(node)
			self.map[key] = Node(key, value, None, None)
			self.addNode(self.map[key])
		else:
		# if key not present, limit check. if no issue, add node 
			if self.curr == self.limit:
				lru = self.tail
				del self.map[lru.key]
				self.deleteNode(lru)	
				self.curr -= 1
			node = Node(key, value, None, None)
			self.map[key] = node
			self.addNode(self.map[key])
			self.curr += 1
					
	def getValue(self, key):
		if key in self.map:
			node = self.map[key]
			self.deleteNode(node)
			self.addNode(node)
			return node.val
		else:
			return -1

lru = LRU(10)
for i in range(15):
	lru.insert(i, i+100)
	lru.printNodes()
lru.printNodes()

for i in range(10, -1, -1):
	print(lru.getValue(i))

lru.printNodes()

lru.insert(9, 9000)
lru.printNodes()

for i in range(15):
	lru.insert(i, i+200)

lru.printNodes()
