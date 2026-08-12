class Solution {
public:
    bool makeEqual(vector<string>& words) {
        if (words.size() == 1) {
            return true;
        }
        vector<int> store(26,0);

        for(string word:words){
            for(char ch:word){
                store[static_cast<int>(ch)- 97]++;
            }
        }
        for(int i=0;i<26;i++){
            if(store[i] % words.size() != 0) return false; 
        }
        return true;
    }
};