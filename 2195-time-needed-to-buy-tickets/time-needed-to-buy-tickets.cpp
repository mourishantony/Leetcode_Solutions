class Solution {
public:
    int timeRequiredToBuy(vector<int>& tickets, int k) {
        int sec = 0;
        int T = tickets[k];
        for(int i=0;i<tickets.size();i++){
            if(i<=k){
                if(tickets[i] < T) sec = sec + tickets[i];
                else sec = sec + T;
            }
            else{
                if(tickets[i] < T) sec = sec + tickets[i];
                else sec = sec + (T - 1);
            }
        }
        return sec;
    }
};