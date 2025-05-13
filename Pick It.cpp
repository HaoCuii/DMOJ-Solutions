#include <bits/stdc++.h>
using namespace std;

//range dp, where dp[i][j] is max of range i,j after everything is cleared
//if you remove the kth element last, your left with ai,ak,aj
//therefore our recurrence is simply dp[i][j] = dp[i,k]+dp[k,j] + dp[i] + dp[k] + dp[j] 


int main(){
    int n;
    while (cin >> n && n != 0) {
        vector<int> nums(n);
        for (int i = 0; i < n; ++i) {
            cin >> nums[i];
        }
        vector<vector<int>> dp(n, vector<int>(n, 0));

        for (int len = 3; len <= n; len++) {
            for (int i = 0; i <= n - len; i++) {
                int j = i + len - 1;
                for (int k = i + 1; k < j; k++) {
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i] + nums[k] + nums[j]);
                }
            }
        }
        
        cout << dp[0][n-1] << '\n';
    }
    return 0;
}