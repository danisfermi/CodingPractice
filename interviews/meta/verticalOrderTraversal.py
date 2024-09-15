class Node:
    def __init__(self, k):
        self.key = k
        self.left = None
        self.right = None

def get_order(root, hd, m):
    if root is None:
        return

    if hd not in m:
        m[hd] = []
    m[hd].append(root.key)

    get_order(root.left, hd - 1, m)

    get_order(root.right, hd + 1, m)

def print_order(root):
    m = {}
    hd = 0

    get_order(root, hd, m)

    for key in sorted(m.keys()):
        for value in m[key]:
            print(value, end=" ")
        print()

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.right = Node(9)
print_order(root)
