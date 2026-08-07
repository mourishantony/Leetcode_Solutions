class Solution {
public:
    int smallestNumber(int n, int t) {
        for(int i=n;1000;i++){
            int abc = i;
            int ans = 1;
            while(abc>0){
                int temp = abc%10;
                if(temp == 0){
                    ans =0;
                    break;
                }
                ans *= temp;
                abc = abc/10;
            }
            if(ans%t == 0) return i;
        }
    }
};