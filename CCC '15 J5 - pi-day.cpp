#include <bits/stdc++.h>
using namespace std;

// dp[i][j] = number of ways to write i as sum of j positive integers
int dp[251][251],n,k;

int main() {
    cin >> n >> k;
    dp[0][0] = 1;

    for (int num = 1; num <= n; num++) {
        for (int i = num; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                dp[i][j] += dp[i - num][j - 1];
            }
        }
    }

    cout << dp[n][k] << '\n';
}
