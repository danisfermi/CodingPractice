class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(root):
            if root is None:
                return False
            a1 = helper(root.left)
            a2 = helper(root.right)
            if not a1:
                root.left = None
            if not a2:
                root.right = None
            return (root.val == 1) or a1 or a2 
        return root if helper(root) else None
