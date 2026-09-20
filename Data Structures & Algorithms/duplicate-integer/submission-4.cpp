class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int, int> dup;
        for(int i = 0; i < nums.size(); ++i){
            cout << nums[i] << "\n";
            if (dup.count(nums[i])){
                return true;
            }
            dup[nums[i]] = 1;
        }
        return false;
    }
};