class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        res = []
        def dfsUtil(v, temp):
            if v == len(graph) - 1:
                res.append(temp)
                return
            for i in graph[v]:
                dfsUtil(i, temp+[i])
        dfsUtil(0, [0])
        return res
