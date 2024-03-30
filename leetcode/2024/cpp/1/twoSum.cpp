class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> s;
        int complement = 0;
        for (int i = 0; i < nums.size(); i++)
        {
            complement = target - nums[i];
            if (s.find(complement) != s.end())
            {
                return {s[complement], i};
            }
            s[nums[i]] = i;
        }
        return {};
    }
};
