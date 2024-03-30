class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> map;
        for(auto st : strs)
        {
            string word = st;
            sort(word.begin(), word.end());
            map[word].push_back(st);
        }
        vector<vector<string>> ans;
        for( auto el : map)
        {
            ans.push_back(el.second);
        }
        return ans;
    }
};
