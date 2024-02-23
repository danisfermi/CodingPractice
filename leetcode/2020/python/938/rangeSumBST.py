class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.res = 0
        def helper(root):
            if root:
                if L <= root.val <= R:
                    self.res += root.val
                if root.val > L:
                    helper(root.left)
                if root.val < R:
                    helper(root.right)
        helper(root)
        return self.res
