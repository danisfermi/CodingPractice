class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        int l = 0, max_ct = 0;
        int max_el = *max_element(nums.begin(), nums.end());
        long long res = 0;
        for(int r = 0; r < nums.size(); r++)
        {
            if (nums[r] == max_el)
            {
                max_ct += 1;
            }
            while ((max_ct > k) or (l <= r and max_ct == k and nums[l] != max_el))
            {
                if (nums[l] == max_el)
                {
                    max_ct -= 1;
                }
                l += 1;
            }
            if (max_ct == k)
                res += (l + 1);
        }
        return res;
    }
};
