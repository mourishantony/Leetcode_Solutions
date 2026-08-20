class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        unordered_map<int,string> store;
        for(int i=0;i<names.size();i++) store[heights[i]] = names[i];
        sort(heights.begin(),heights.end(),greater<int>());
        vector<string> ans;
        for(int i=0;i<names.size();i++) ans.push_back(store[heights[i]]);
        return ans;
    }
};