using namespace std;

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() == 1){
            return 0;
        }

        int profit = 0;

        int b = 0;

        for(int i =1; i < prices.size(); i++){
            int r = prices[i] - prices[b];

            if (r > profit){
                profit = r;
            }

            if (prices[i] < prices[b]){
                b = i;
            }
        }
        return profit;
    }
};
