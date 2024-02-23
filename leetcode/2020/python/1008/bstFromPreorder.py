class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        def helper(root, val):
            if root.val > val:
                if root.left:
                    helper(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                if root.right:
                    helper(root.right, val)
                else:
                    root.right = TreeNode(val)
        for i in xrange(1,len(preorder)):
            helper(root, preorder[i])
        return root
