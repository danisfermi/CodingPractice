class Solution {
public:
    int lengthOfLastWord(string s) {
        int i = s.size() - 1;
        while (s[i] == ' ')
        {
            i -= 1;
        }
        int res = 0;
        while (i >= 0  && s[i] != ' ')
        {
            res += 1;
            i -= 1;
        }
        return res;
    }
};
