class Solution {
public:
    bool isMonotonic(vector<int>& nums) {
        return inc(nums) || dec(nums);
    }
    int inc(vector<int>& nums){
        int prev = nums[0];
        for(int num : nums){
            if(num < prev){
                return false;
            }
            prev = num;
        }
        return true;
    }

    int dec(vector<int>& nums){
        int prev = nums[0];
        for(int num : nums){
            if(num > prev){
                return false;
            }
            prev = num;
        }
        return true;
    }
};