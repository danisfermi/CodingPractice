class Solution {
public:
    bool checkPal(string &s, int i, int j) {
        while (i < j) {
            if (s[i] != s[j])
                return false;
            i += 1;
            j -= 1;
        }
        return true;
    }
    void helper(int idx, vector<string> &temp, vector<vector<string>> &result, string &s) {
        if (idx == s.size()) {
            result.push_back(temp);
            return;
        }
        for(int i = idx; i < s.size(); i++){
            if(checkPal(s, idx, i)){
                temp.push_back(s.substr(idx, i - idx + 1));
                helper(i + 1, temp, result, s);
                temp.pop_back();
            }
        }
    }
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> temp;
        helper(0, temp, res, s);
        return res;
    }
};
