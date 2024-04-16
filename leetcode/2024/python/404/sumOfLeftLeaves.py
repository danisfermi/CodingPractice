# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(root, flag):
            if not root:
                return 0
            if flag == 0 and not root.right and not root.left:
                return root.val
            return (helper(root.left, 0) + helper(root.right, 1))
        return helper(root, 1)
    
    
