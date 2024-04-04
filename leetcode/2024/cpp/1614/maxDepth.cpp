class Solution {
public:
    int maxDepth(string s) {
        int res = 0, inc = 0;
        for(int i = 0; i < s.size(); i++)
        {
            if (s[i] == '(')
            {
                inc += 1;
            }
            if (s[i] == ')')
            {
                inc -= 1;
            }
            res = (res > inc) ? res : inc;
        }
        return res;
    }
};
