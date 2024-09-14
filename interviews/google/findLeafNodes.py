'''
For a rooted tree with any arbitary number of children for each node,
not necessarily n-ary tree.
Remove all the leaf nodes, and store them in a list, this would create
new leaf nodes. Repeat untill all the nodes are removed
Conditions : Freshly created leaf nodes(node whose children are removed)
should not be removed just after its children are removed, unless
there's no other option for us, then we can remove it
'''

from collections import defaultdict

res = defaultdict(list)

def helper(node, dels):
	if node is None:
		return dels
	maxDels = dels
	for n in node.children:
		maxDels = max(maxDels, helper(n, dels))
	res[maxDels].append(node.val)
	return maxDels + 1	

def findLeafNodes(root):
	helper(root, 0)
	return res
	
class Node:
    def __init__(self, data):
        self.val = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)

root = Node(1)
child1 = Node(2)
child2 = Node(3)
child3 = Node(4)
child4 = Node(5)

root.add_child(child1)
root.add_child(child2)
child1.add_child(child3)
child1.add_child(child4)

print(findLeafNodes(root))

