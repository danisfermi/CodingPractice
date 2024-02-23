class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        def helper(root, level):
            if root is None:
                return
            if len(self.res)-1 >= level:
                self.res[level] = root.val
            else:
                self.res.append(root.val)
            helper(root.left, level+1)
            helper(root.right, level+1)
        helper(root, 0)
        return self.res
