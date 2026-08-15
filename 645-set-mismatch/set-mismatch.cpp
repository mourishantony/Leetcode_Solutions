class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        sort(nums.begin() , nums.end());
        int l =0,r = 0;
        if(nums[0] != 1) r=1;
        for(int i=1;i<nums.size();i++){
            if(nums[i] == nums[i-1]) l = nums[i];
            else if(nums[i]-1 != nums[i-1]) r = nums[i] -1;

            if(l>0 && r>0) break;
        }
        if(r==0) r = nums.size();
        return {l,r};
    }
};