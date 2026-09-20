class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> res;
        map<int, int> m;
        for(int i = 0; i < nums.size(); ++i){
            m[nums[i]]+=1;
        }

        vector<pair<int, int>> pairs;
        for( auto const& [key, val] : m){
            pairs.push_back({val, key});
        }
        make_heap(pairs.begin(), pairs.end());

        for(int i = 0; i < k; ++i){
            pop_heap(pairs.begin(), pairs.end());
            res.push_back(pairs.back().second); // Get the number, not frequency
            pairs.pop_back();
        }
        return res;
        
    }
};
