class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = {}
        def dfs(root, level):
            if root:
                if root.left:
                    dfs(root.left, level+1)
                if root.right:
                    dfs(root.right, level+1)
                if level in res:
                    res[level] += root.val
                else:
                    res[level] = root.val
        dfs(root,0)
        return res[max(res)]
