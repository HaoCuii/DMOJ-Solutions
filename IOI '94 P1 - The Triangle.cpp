#include <bits/stdc++.h>
using namespace std;

int n;
int a[102][102];
int dp[102][102];

int main(){
    cin >> n;
    for (int i = 1; i <= n; i++){
        for (int j = 1; j <= i; j++){
            cin >> a[i][j];
        }
    }
    for (int j = 1; j <= n; j++) {
        dp[n][j] = a[n][j];
    }
    for (int i = n - 1; i >= 1; i--) {
        for (int j = 1; j <= i; j++) {
            dp[i][j] = a[i][j] + max(dp[i+1][j], dp[i+1][j+1]);
        }
    }

    cout << dp[1][1] << endl;
    return 0;
}
