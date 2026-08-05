class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        if(ransomNote.size() > magazine.size()){
            return false;
        }
        unordered_map<char,int> ans;
        for(char i : ransomNote) ans[i]++;

        for(const auto& a:ans){
            if(count(magazine.begin(),magazine.end(),a.first) < a.second){
                return false;
            }
        }
        return true;
    }
};