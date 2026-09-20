class Solution {
public:
    int lengthOfLongestSubstring(std::string s) {
        if (s.empty()) return 0;
        
        std::unordered_set<char> chars;
        int res = 0;
        int l = 0;
        
        for (int r = 0; r < s.length(); r++) {
            // If we find a duplicate, remove chars from left until no duplicate
            while (chars.count(s[r])) {
                chars.erase(s[l]);
                l++;
            }
            
            // Add current character
            chars.insert(s[r]);
            
            // Update max length
            res = std::max(res, r - l + 1);
        }
        
        return res;
    }
};