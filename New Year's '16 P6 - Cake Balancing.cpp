#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int l, r, w;
    cin >> l >> r >> w;

    vector<int> li(l), ri(r);
    for (int i = 0; i < l; i++) cin >> li[i];
    for (int i = 0; i < r; i++) cin >> ri[i];
    int fullL = (1 << l) - 1;
    int fullR = (1 << r) - 1;

    vector<int> sumL(1 << l, 0), sumR(1 << r, 0);
    for (int mask = 0; mask <= fullL; ++mask)
        for (int i = 0; i < l; ++i)
            if (mask & (1 << i)) sumL[mask] += li[i];

    for (int mask = 0; mask <= fullR; ++mask)
        for (int i = 0; i < r; ++i)
            if (mask & (1 << i)) sumR[mask] += ri[i];

    vector<vector<int>> dp(1 << l, vector<int>(1 << r, -1));
    deque<pair<int, int>> dq;
    dp[fullL][fullR] = 0;
    dq.push_back({fullL, fullR});

    while (!dq.empty()) {
        auto [lmask, rmask] = dq.front(); dq.pop_front();
        int steps = dp[lmask][rmask];
        for (int sub = lmask; sub; sub = (sub - 1) & lmask) {
            int newL = lmask ^ sub;
            int lsum = sumL[newL], rsum = sumR[rmask];
            if (abs(lsum - rsum) <= w && dp[newL][rmask] == -1) {
                dp[newL][rmask] = steps + 1;
                dq.push_back({newL, rmask});
            }
        }
        for (int sub = rmask; sub; sub = (sub - 1) & rmask) {
            int newR = rmask ^ sub;
            int lsum = sumL[lmask], rsum = sumR[newR];
            if (abs(lsum - rsum) <= w && dp[lmask][newR] == -1) {
                dp[lmask][newR] = steps + 1;
                dq.push_back({lmask, newR});
            }
        }
    }

    cout << dp[0][0] << "\n";
    return 0;
}
