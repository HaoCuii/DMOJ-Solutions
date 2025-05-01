    #include <bits/stdc++.h>
    using namespace std;


    int main(){
        int n,k; cin >> n >> k;
        vector<int> moves; 
        for (int i = 0; i < n; i++){
            int val; cin >> val; moves.push_back(val);
        }

        vector<bool> dp(k+1, false); 
        for (int i = 0; i <= k; i++){
            for (int move: moves){
                if (i-move >= 0 && !dp[i-move]){
                    dp[i] = true;
                    break;
                }
            }
        }
        
        if (dp[k]) {
            cout << "First";
        }
        else {
            cout << "Second";
        }
        return 0;
    }