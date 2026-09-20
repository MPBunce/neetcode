class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int l = 0;
        int r = 1;
        int profit = 0;
        while (r < prices.size()){
            int diff = prices[r] - prices[l];
            cout << diff << " = " << prices[r] << " - "<< prices[l] <<endl;
            if(profit < diff){
                profit = diff;
            }

            if( prices[r] < prices[l] ){
                l = r;
                r += 1;
            } else {
                r += 1;
            }

        }
        return profit;
    }
};
