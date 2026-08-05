class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        int alpha[26] = {0};

        for(char a : magazine) alpha[a - 'a']++;

        for(char a:ransomNote) if(alpha[a-'a']-- <=0) return false;

        return true;
    }
};