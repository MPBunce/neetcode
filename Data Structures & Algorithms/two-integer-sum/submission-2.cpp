class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> res;
        map<int, int> m;

        for(int i = 0; i < nums.size(); ++i){
            int match = target - nums[i];
            if( m.count(match) ){
                res.push_back(m[match]);
                res.push_back(i);
                return res;
            } else {
                m[nums[i]] = i;
            }
        }

        return res;
    }
};
