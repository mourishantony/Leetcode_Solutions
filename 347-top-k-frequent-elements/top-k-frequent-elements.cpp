class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        if(nums.size() ==1)return nums;
        unordered_map<int,int> store ;
        for(int num:nums) store[num]++;
        vector<vector<int>> bucket;
        for(int i=0;i<nums.size()+1;i++) bucket.push_back({});
        for(const auto& [key, value] : store){
            bucket[value].push_back(key);
        }
        vector<int> ans;

        for(int key = nums.size();key >= 0;key--){
            for(int num:bucket[key]){
                ans.push_back(num);

                if(ans.size() == k) return ans;
            }
        }
        return ans;
    }
};