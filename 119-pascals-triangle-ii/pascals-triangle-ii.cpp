class Solution {
public:
    vector<int> getRow(int rowIndex) {
        if(rowIndex == 1) return {1,1};
        vector<int> ans = {1};
        while(rowIndex > 0){
            ans.insert(ans.end(),0);
            ans.insert(ans.begin(),0);
            vector<int> temp = {};
            int i=0,j=1;
            while(j<ans.size()){
                temp.push_back(ans[i]+ans[j]);
                i++;
                j++;
            }
            ans = temp;
            rowIndex--;
        }

        return ans;
    }
};