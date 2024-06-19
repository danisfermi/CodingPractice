class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        m = collections.defaultdict(list)
        for w in wordList:
            for i in range(len(w)):
                key = w[:i] + "*" + w[i+1:]
                m[key].append(w)
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        while q:
            for i in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                for i in range(len(w)):
                    key = w[:i] + "*" + w[i+1:]
                    for neiWord in m[key]:
                        if neiWord not in visit:
                            visit.add(neiWord)
                            q.append(neiWord)
            res += 1
        return 0
