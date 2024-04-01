class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        reverse(digits.begin(), digits.end());
        int i = 0;
        int carry = 1, s = 0;
        while (carry)
        {
            if (i < digits.size())
            {
                if (digits[i] == 9)
                {
                    digits[i] = 0;
                }
                else
                {
                    digits[i] += 1;
                    carry = 0;
                }
            }
            else
            {
                digits.push_back(1);
                carry = 0;
            }
            i += 1;
        }
        reverse(digits.begin(), digits.end());
        return digits;
    }
};
