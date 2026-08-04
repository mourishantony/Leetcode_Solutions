class Solution {
public:
    int countConsistentStrings(string allowed, vector<string>& words) {
        set<int> all(allowed.begin(),allowed.end());
        int count =0;
        for(string word:words){
            for(char ch:word){
                if(!all.contains(ch)){
                    count++;
                    break;
                }
            }
        }
        return words.size() - count;
    }
};