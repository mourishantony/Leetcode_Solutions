class Solution {
public:
    string largestGoodInteger(string num) {
        int ans = 0;
        bool flag = false;
        int a = 0,b = 1, c = 2;
        while(c < num.size()){
            if(num[a] == num[b] && num[a] == num[c]){
                flag = true;
                if(num[a] > ans) ans = num[a]; 
            }
            a++;
            b++;
            c++;
        }
        if(flag) 
            return string(3,ans);
        else 
            return "";
    }
};