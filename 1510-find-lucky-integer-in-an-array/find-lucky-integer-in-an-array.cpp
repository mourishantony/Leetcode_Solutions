class Solution {
public:
    int findLucky(vector<int>& arr) {
        unordered_map<int,int> freq;
        int res = -1;
        for(int num:arr){
            freq[num]++;
        }

        for(auto it:freq){
            if(it.first == it.second){
                res = max(res,it.first);
            }
        }
        return res;
        
    }
};