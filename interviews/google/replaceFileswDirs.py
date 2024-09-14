'''
Replace files with directories if all files in directory are
specified
Example input & output:
allFiles = [
"a/b/c/d.txt",
"a/b/c/e.txt",
"a/b/b.txt",
"a/b/e.txt",
"b/c/d.txt"
]
subsetFiles = [
"a/b/c/d.txt",
"a/b/c/e.txt",
"a/b/b.txt",
"b/c/d.txt"
]
output=[
"a/b/c",
"a/b/b.txt",
"b"
]
'''

class Node:
	def __init__(self, val = "?"):
		self.val = val
		self.children = {}
		self.eow = False
		self.count = 0

class Trie:
	def __init__(self):
		self.root = Node()

	def insert(self, word):
		word = word.split("/")
		node = self.root
		for w in word:
			if w not in node.children:
				node.children[w] = Node(w)
			node.count += 1
			node = node.children[w]
		node.eow = True
	
	def delete(self, word):
		word = word.split("/")
		node = self.root
		for w in word:
			if w not in node.children:
				return
			node.count -= 1
			node = node.children[w]
		node.eow = True

res = []
def generateOutput(node, st):
	print(node.val, node.count)
	if node.count == 0:
		res.append(st)
		return res
	for child in node.children:
		generateOutput(node.children[child], st + child + "/")
	return [s[:-1] for s in res]

allFiles = [
"a/b/c/d.txt",
"a/b/c/e.txt",
"a/b/b.txt",
"a/b/e.txt",
"b/c/d.txt"
]

subsetFiles = [
"a/b/c/d.txt",
"a/b/c/e.txt",
"a/b/b.txt",
"b/c/d.txt"
]

trie = Trie()
for file in allFiles:
	trie.insert(file)

for file in subsetFiles:
	trie.delete(file)

print(generateOutput(trie.root, ""))
