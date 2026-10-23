class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m; 
        for (const auto &num : nums) m[num] += 1; 
        vector<vector<int>> v(nums.size() + 1);  
        for (const auto &[num, freq] : m) {
          v[freq].push_back(num); 
        }

        vector<int> ret; 
        for (int i = v.size() - 1; i >= 0; i--) {
            if (v[i].size() != 0) {
                for (const auto &num : v[i]) {
                    if (ret.size() < k) {
                        ret.push_back(num);
                    }
                }
            }
        }
        return ret;  
    }
};
