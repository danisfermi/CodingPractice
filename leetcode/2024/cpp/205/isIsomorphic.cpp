class Solution {
public:
    bool isIsomorphic(string s, string t) {
        int l1 = s.size(), l2 = t.size();
        if (l1 != l2)
            return false;
        unordered_map<char, char> m1, m2;
        char c1, c2;
        for(int i = 0; i < l1; i++)
        {
            c1 = s[i];
            c2 = t[i];
            if ((m1.count(c1) != 0 && m1[c1] != c2) || (m2.count(c2) != 0 && m2[c2] != c1))
            {
                return false;
            }
            m1[c1] = c2;
            m2[c2] = c1;
        }
        return true;
    }
};
