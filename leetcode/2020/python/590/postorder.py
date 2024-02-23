class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.res = []
        def helper(root):
            if root is None:
                return
            for i in root.children:
                helper(i)
            self.res.append(root.val)
        helper(root)
        return self.res
