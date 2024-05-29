# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def helper(node, level):
            if node is None:
                return
            #print(node.val, level, res)
            if len(res) >= (level + 1):
                res[level].append(node.val)
            else:
                res.append([node.val])
            helper(node.left, level + 1)
            helper(node.right, level + 1)
        helper(root, 0)
        return res
        
