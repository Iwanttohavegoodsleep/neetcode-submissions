class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> m;  
        vector<int> key; 
        vector<int> value; 
        vector<int> ret; 

        for (int i = 0; i < nums.size(); ++i) {
            m[nums[i]] = m[nums[i]] + 1; 
        }

        for (const auto& pair : m) {
           key.push_back(pair.first); // key
           value.push_back(pair.second);  // value 
        }
        
        for (int i = 0; i < k; i++) {
            auto max_val = max_element(value.begin(), value.end());
            for (int j = 0; j < key.size(); j++) {
                if (m[key[j]] == *max_val) {
                   ret.push_back(key[j]); 

                   value.erase(value.begin() + j); 
                   key.erase(key.begin() + j); 
                   break; 
                }
            }
        }

        return ret; 
    }
};
