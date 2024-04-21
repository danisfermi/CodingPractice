class Solution {
public:
    vector<int> deckRevealedIncreasing(vector<int>& deck) {
        int n = deck.size();
        vector<int> res(n);
        queue<int> dq;
        for (int i = 0; i < n; i++)
            dq.push(i);
        sort(deck.begin(), deck.end());
        for(int i = 0; i < n; i++) {
            res[dq.front()] = deck[i];
            dq.pop();
            if (!dq.empty()) {
                dq.push(dq.front());
                dq.pop();
            }
        }
        return res;
    }
};
