class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        hasparent = set(leftChild+rightChild)
        hasparent.discard(-1)
        if len(hasparent) == n:
            return False
        root = -1
        for i in range(n):
            if i not in hasparent:
                root = i
                break
        visit = set()
        def dfs(i):
            if i == -1:
                return True
            if i in visit:
                return False
            visit.add(i)
            return dfs(leftChild[i]) and dfs(rightChild[i])
        return dfs(root) and len(visit) == n
