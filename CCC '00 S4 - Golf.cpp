#include <bits/stdc++.h>
using namespace std;

using ll = long long;

// dp[i] stores the minimum number of strokes to reach the ith meter
const ll INF = 1e18;
ll dp[5400];
vector<ll> clubs;

int main() {
    int dist, n;
    cin >> dist >> n;
    fill(dp, dp + 5400, INF);
    dp[0] = 0;

    for (int i = 0; i < n; i++) {
        ll club; cin >> club; clubs.push_back(club);
    }

    for (int i = 0; i <= dist; i++) {
        if (dp[i] == INF) continue; 
        for (ll club : clubs) {
            dp[i + club] = min(dp[i + club], dp[i] + 1);
        }
    }
    

    if (dp[dist] != INF) {
        cout << "Roberta wins in " << dp[dist] << " strokes.\n";
    } else {
        cout << "Roberta acknowledges defeat.\n";
    }

    return 0;
}
