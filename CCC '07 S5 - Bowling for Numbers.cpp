/*
dp[i][k] is the max obtainable from the i'th index onwards with k balls left? 
Transition start from 0 balls and work backwards. Computing each index too.
No clue if this will work.
*/

#include <bits/stdc++.h>
using namespace std;

int main(){
    int t; cin >> t;
    for (int _ = 0; _ < t; _++){
        int n, k, w; cin >> n >> k >> w;
        vector<vector<int>> dp(n+1, vector<int>(k+1));
        vector<int> pins(n);
        for (int i = 0; i < n; i++){
            cin >> pins[i];
        }

        vector<int> suf(n + 1, 0);
        for (int i = n - 1; i >= 0; i--) suf[i] = suf[i + 1] + pins[i];

        vector<int> sum(n, 0);
        for (int i = 0; i < n; i++){
            int r = min(n, i + w);
            sum[i] = suf[i] - suf[r];
        }


        for (int b = 1; b <= k; b++){
            for (int i = n-1; i >= 0; i--){
                if (i+w < n){
                    dp[i][b] = max(dp[i+1][b], sum[i] + dp[i+w][b-1]);
                }
                else{
                    dp[i][b] = sum[i];
                }
            }
        }
        cout << dp[0][k] << '\n';
    }
    return 0;
}