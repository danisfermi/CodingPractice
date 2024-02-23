# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        self.res = []
        def helper(node, level):
            if node is None:
                return
            if len(self.res) < level + 1:
                self.res.append([node.val])
            else:
                self.res[level].append(node.val)
            helper(node.left, level+1)
            helper(node.right, level+1)
        helper(root, 0)
        for level, arr in enumerate(self.res):
            if level % 2 == 0:
                prev = -float('inf')
            else:
                prev = float('inf')
            for el in arr:
                if level % 2 == 0:
                    if el % 2 == 0 or el <= prev:
                        return False
                else:
                    if el % 2 != 0 or el >= prev:
                        return False
                prev = el
        return True
                
