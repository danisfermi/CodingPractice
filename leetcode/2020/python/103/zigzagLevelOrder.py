class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.res = []
        def helper(root, level):
            if root is None:
                return
            if len(self.res) - 1 >= level:
                if level % 2 == 0:
                    self.res[level].append(root.val)
                else:
                    self.res[level].insert(0, root.val)
            else:
                self.res.append([root.val])
            helper(root.left, level+1)
            helper(root.right, level+1)
        helper(root, 0)
        return self.res
