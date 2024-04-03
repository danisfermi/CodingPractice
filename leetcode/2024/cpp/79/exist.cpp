class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        int ROWS = board.size();
        int COLS = board[0].size();
        unordered_set<pair<int, int>> path;
        
        for(int i = 0; i < ROWS; i++)
        {
            for(int j = 0; i < COLS; j ++)
            {
                if (dfs(i, j, 0, board, word, ROWS, COLS, path))
                {
                    return true;
                }
            }
        }
        return false;
    }
    
private:
    bool dfs(int i, int j, int k, vector<vector<char>>& board, string word, int ROWS, int COLS, unordered_set<pair<int, int>> path)
    {
            if(k == word.size()) {
                return false;
            }
            
            if ((i < 0) || (j < 0) || (i >= ROWS) || (j >= COLS) || (board[i][j] != w[k]) || (path.count(make_pair(i, j)) != 0))
            {
                return false;
            }
            path.insert(make_pair(i, j));
            if (dfs(i+1, j, k+1, board, word, ROWS, COLS, path) || dfs(i-1, j, k+1, board, word, ROWS, COLS, path) || dfs(i, j+ 1, k+1, board, word, ROWS, COLS, path) || dfs(i, j-1, k+1, board, word, ROWS, COLS, path))
            {
                return true;
            }
            path.erase(make_pair(i, j));
            return false;
    }
};
