class Solution {
public:
    vector<string> commonChars(vector<string>& words) {
        string a = words[0];
        vector<string> ans;

        for(char i:a){
            ans.push_back(string(1, i));
            for(int j=1;j<words.size();j++){
                if(!words[j].contains(i)){
                    ans.erase(find(ans.begin(),ans.end(),string(1,i)));
                    break;
                }
                else{
                    words[j].erase(words[j].find(i),1);
                }
            }
        }
        return ans;
    }
};