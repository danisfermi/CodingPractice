class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        def helper(root1, root2):
            if root1 is None and root2 is None:
                return None
            root = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
            root.left = helper(root1.left if root1 else None, root2.left if root2 else None)
            root.right = helper(root1.right if root1 else None, root2.right if root2 else None) 
            return root
        return helper(t1, t2)
