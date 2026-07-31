class Solution {
public:
    bool divideArray(vector<int>& nums) {
        unordered_set<int> ans;
        for(int num : nums){
            if(!ans.contains(num)){
                ans.insert(num);
            }
            else{
                ans.erase(num);
            }
        }
        return ans.size() == 0 ;
    }
};