class Solution:
    def validate(self, val):
        if val < 0 or val > 9:
            return False
        if val in self.m:
            return False
        self.m.add(val)
        return True
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        self.m = set()
        for i in range(rows):
            self.m = set()
            for j in range(cols):
                if board[i][j] != "." and not self.validate(int(board[i][j])):
                    return False
        self.m = set()
        for j in range(cols):
            self.m = set()
            for i in range(rows):
                if board[i][j] != "." and not self.validate(int(board[i][j])):
                    return False
        self.m = set()
        for k in [[0,0], [0,3], [3,3],[3,0],[6,0],[0,6],[6,3],[3,6],[6,6]]:
            self.m = set()
            for i in range(k[0], k[0] + 3):
                for j in range(k[1], k[1]+3):
                    if board[i][j] != "." and not self.validate(int(board[i][j])):
                        return False
        return True
                
