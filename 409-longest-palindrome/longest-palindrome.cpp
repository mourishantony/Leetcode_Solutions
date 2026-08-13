class Solution {
public:
    int longestPalindrome(string s) {
        if(s.size() == 1) return 1;
        unordered_map<char,int> counter;
        for(char c:s)counter[c]++;
        int count =0;
        bool flag = true;
        for(const auto& pair:counter){
            if(pair.second %2 != 0){
                count = count + pair.second -1;
                if(flag){
                    count++;
                    flag = false;
                }
            }
            else count = count + pair.second;
        }
        return count;

    }
};