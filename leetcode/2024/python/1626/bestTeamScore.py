class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [[scores[i], ages[i]] for i in range(len(scores))]
        pairs.sort()
        dp = [pairs[i][0] for i in range(len(pairs))]
        for i in range(len(pairs)):
            mScore, mAge = pairs[i]
            for j in range(i):
                score, age = pairs[j]
                if age <= mAge:
                    dp[i] = max(dp[i], mScore + dp[j])
        return max(dp)          
        '''
        pairs = [[scores[i], ages[i]] for i in range(len(scores))]
        pairs.sort()
        dp = {}
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i,j)]
            if i == len(pairs):
                return 0
            mScore, mAge = pairs[j] if j > 0 else [0, 0]
            score, age = pairs[i]
            res = 0
            if (score > mScore and age < mAge):
                res = dfs(i+1, i) + score
            dp[(i, j)] = max(res, dfs(i+1, j))
            return dp[(i, j)]
        return dfs(0, -1)
        '''
