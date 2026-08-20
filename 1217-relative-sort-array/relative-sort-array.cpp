class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        unordered_map<int,int> store;
        for(int arr : arr1){
            store[arr]++;
        }
        vector<int> ans;
        for(int arr:arr2){
            for(int i=0;i<store[arr];i++) ans.push_back(arr);
            erase(arr1,arr);
        }
        sort(arr1.begin(),arr1.end());
        ans.insert(ans.end(),arr1.begin(),arr1.end());
        return ans;
        
    }
};