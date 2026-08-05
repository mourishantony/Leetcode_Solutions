class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_set<string> s ={};
        for(auto &path:paths) s.insert(path[0]);

        for(auto &path:paths) if(!s.contains(path[1])) return path[1];
        return "";
    }
};