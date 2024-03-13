class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        l = len(board)
        board.reverse()
        def intToPos(square):
            row = (square - 1 ) // l
            col = (square - 1) % l
            if row % 2:
                col = l - col - 1
            return [row, col]
        q = deque()
        q.append((1, 0)) # square, moves
        visit = set()
        while q:
            square, moves = q.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                row, col = intToPos(nextSquare)
                if board[row][col] != -1:
                    nextSquare = board[row][col]
                if nextSquare == l * l:
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    q.append((nextSquare, moves + 1))
        return -1
        
