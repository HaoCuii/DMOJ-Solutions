#include <bits/stdc++.h>
using namespace std;

//dp[i][j] is the minimum lost area for rectangle i,j
//Bottom's up approach

int dp[601][601];
int w, h, n;

int main(){
    for (int i = 0; i <= 600; i++) {
        for (int j = 0; j <= 600; j++) {
            dp[i][j] = i*j;
        }
    }
    cin >> w >> h;
    cin >> n;
    for (int i = 0; i < n; i++){
        int a,b; cin >> a >> b;
        dp[b][a] = 0;
    }
    for (int i = 1; i <= h; i++) {
        for (int j = 1; j <= w; j++) {
            if (dp[i][j] == 0) continue;

            for (int k = 1; k < i; k++) {
                dp[i][j] = min(dp[i][j], dp[k][j] + dp[i - k][j]);
            }
            for (int k = 1; k < j; k++) {
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[i][j - k]);
            }
        }
    }

    cout << dp[h][w];
    return 0;
}