class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        def util(root, level):
            if root is None:
                return
            if level <= len(self.res)-1:
                self.res[level].append(root.val)
            else:
                self.res.append([root.val])
            util(root.left, level+1)
            util(root.right, level+1)
        util(root, 0)
        return self.res
