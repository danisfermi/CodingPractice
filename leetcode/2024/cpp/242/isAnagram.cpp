class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> map;
        for (auto a : s)
        {
            map[a] += 1;
        }
        for (auto a : t)
        {
            map[a] -= 1;
        }
        for (auto a: map)
        {
            if (a.second != 0)
            {
                return false;
            }
        }
        return true;
    }
};
