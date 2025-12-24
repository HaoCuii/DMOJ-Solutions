#include <bits/stdc++.h>
using namespace std;

int n;
long long a[3000], dp[3000][3000];

int main() {
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
        dp[i][i] = a[i];
    }

    for (int length = 2; length <= n; length++) {
        for (int l = 0; l + length - 1 < n; l++) {
            int r = l + length - 1;
            dp[l][r] = max(a[l] - dp[l+1][r], a[r] - dp[l][r-1]);
        }
    }

    cout << dp[0][n-1] << '\n';
    return 0;
}
