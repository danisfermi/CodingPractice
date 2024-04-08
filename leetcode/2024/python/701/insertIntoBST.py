# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        cur = root
        while True:
            if val > cur.val:
                if cur.right is None:
                    cur.right = TreeNode(val)
                    return root
                else:
                    cur = cur.right
            else:
                if cur.left is None:
                    cur.left = TreeNode(val)
                    return root
                else:
                    cur = cur.left
            
