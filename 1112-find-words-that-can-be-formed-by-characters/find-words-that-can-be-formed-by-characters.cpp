class Solution {
public:
    int countCharacters(vector<string>& words, string chars) {
        int total = 0;
        for(string word:words){
            bool flag = true;
            for(char ch : word){
                if(count(word.begin(),word.end(),ch) > count(chars.begin(),chars.end(),ch)){
                    flag = false;
                    break;
                }
            }
            if(flag){
                total += word.size();
            }
        }
        return total;
    }
};