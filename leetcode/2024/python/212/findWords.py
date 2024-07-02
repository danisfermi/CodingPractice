class Node:
    def __init__(self):
        self.children = {}
        self.eow = False
        
    def addWord(self, w):
        temp = self
        for c in w:
            if c not in temp.children:
                temp.children[c] = Node()
            temp = temp.children[c]
        temp.eow = True
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Node()
        for w in words:
            trie.addWord(w)
        ROWS, COLS = len(board), len(board[0])
        res = set()
        visit = set()
        def dfs(r, c, node, word):
            if (r < 0) or (c < 0) or (r == ROWS) or (c == COLS) or ((r,c) in visit) or (board[r][c] not in node.children):
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.eow:
                res.add(word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
            visit.remove((r,c))
                
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie, "")
                
        return list(res)
