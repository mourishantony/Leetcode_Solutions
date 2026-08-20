class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector<pair<int,string>> store;
        for(int i=0;i<names.size();i++) store.push_back({heights[i],names[i]});
        sort(store.rbegin(),store.rend());
        vector<string> ans;
        for(int i=0;i<names.size();i++) ans.push_back(store[i].second);
        return ans;
    }
};