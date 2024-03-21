# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def helper(node, val):
            if node is None:
                return
            if node.left is None and node.right is None:
                self.res += (val * 10 + node.val)
                return
            helper(node.left, val * 10 + node.val)
            helper(node.right, val * 10 + node.val)
            return
        helper(root, 0)
        return self.res
