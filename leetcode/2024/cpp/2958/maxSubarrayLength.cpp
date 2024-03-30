class Solution {
public:
    int maxSubarrayLength(vector<int>& nums, int k) {
        int ans = 0, start = 0;
        unordered_map<int, int> frequency;
        for (int end = 0; end < nums.size(); end++) {
            frequency[nums[end]]++;
            while (frequency[nums[end]] > k) {
                frequency[nums[start]]--;
                start++;
            }
            ans = max(ans, end - start + 1);
        }
        return ans;
    }
};
