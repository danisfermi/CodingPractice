class Solution(object):
    def getAllElements(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        self.arr1 = []
        def helper(root):
            if root is None:
                return
            helper(root.left)
            self.arr1.append(root.val)
            helper(root.right)
        helper(root1)
        helper(root2)
        self.arr1.sort()
        return self.arr1
