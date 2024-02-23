iclass Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 0
        def helper(parent, root):
            if parent.val % 2 == 0:
                if root.left:
                    self.res += root.left.val
                if root.right:
                    self.res += root.right.val
            if root.left:
                helper(root, root.left)
            if root.right:
                helper(root, root.right) 
        parent = TreeNode(-1)
        parent.left = root
        parent.right = root
        helper(parent, root)
        return self.res
