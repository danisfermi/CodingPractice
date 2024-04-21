class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        int n = nums.size() - 1;
        vector<int> ans1;
        vector<int> ans2;

        int start = 0;
        int end = n;
        while (start <= end)
        {
            int startsq = nums[start] * nums[start];
            int endsq = nums[end] * nums[end];
            if (startsq > endsq)
            {
                ans1.push_back(startsq);
                start++;
            }
            else
            {
                ans1.push_back(endsq);
                end--;
            }
        }

        for (int i = n; i >= 0; i--)
        {
            ans2.push_back(ans1[i]);
        }
        return ans2;
    }
};
