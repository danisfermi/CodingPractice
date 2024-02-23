class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return TreeNode(val)
        def helper(root, val):
            if not root:
                return
            if val > root.val:
                if root.right:
                    helper(root.right, val)
                else:
                    root.right = TreeNode(val)
            else:
                if root.left:
                    helper(root.left, val)
                else:
                    root.left = TreeNode(val)
        helper(root, val)
        return root
