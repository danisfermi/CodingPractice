class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.res = []
        def helper(root):
            if root is None:
                return
            self.res.append(root.val)
            for i in root.children:
                helper(i)
        helper(root)
        return self.res
