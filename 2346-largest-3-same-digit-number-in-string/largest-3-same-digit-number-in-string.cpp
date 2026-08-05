class Solution {
public:
    string largestGoodInteger(string num) {
        char ans = 0;

        for (int i = 0; i + 2 < num.size(); i++) {
            if (num[i] == num[i + 1] && num[i] == num[i + 2]) {
                ans = max(ans, num[i]);
            }
        }

        if (ans == 0)
            return "";

        return string(3, ans);
    }
};