class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def helper(arr):
            if len(arr) == 0:
                return None
            root = TreeNode(max(arr))
            idx = arr.index(max(arr))
            root.left = helper(arr[:idx])
            root.right = helper(arr[idx+1:])
            return root
        return helper(nums)
