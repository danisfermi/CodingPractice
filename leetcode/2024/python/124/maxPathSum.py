# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.res = root.val
        def helper(node):
            if node is None:
                return 0
            leftMax = helper(node.left)
            rightMax = helper(node.right)
            leftMax = max(0, leftMax)
            rightMax = max(0, rightMax)
            self.res = max(self.res, node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)
        helper(root)
        return self.res
