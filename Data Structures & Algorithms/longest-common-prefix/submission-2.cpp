class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string v = ""; 
        char check; 
        
        for (int i = 0; i < strs[0].size(); i++) {
            if (strs.size() > 0) {
                check = strs[0][i]; 
            }
            for (int j = 0; j < strs.size(); j++) {
                if (strs[j][i] != check) {
                    return v; 
                }
            }
            v.push_back(check); 

        }
          
        return v;   
    }
};