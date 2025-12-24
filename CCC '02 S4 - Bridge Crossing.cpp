#include <bits/stdc++.h>
using namespace std;

// dp[i] - minimum time for the first i people
int m, n;

int main() {
    cin >> m >> n;

    vector<int> times(n); 
    vector<string> names(n); 
    vector<pair<int, vector<int>>> dp(n + 1, {INT_MAX, {}});

    for (int i = 0; i < n; i++) {
        cin >> names[i] >> times[i];
    }
    dp[0] = {0, {}};

    for (int i = 1; i <= n; i++) {
        for (int len = 1; len <= m; len++) {
            int l = i - len;
            int r = i - 1;
            if (l >= 0) {
                int seg_max = *max_element(times.begin() + l, times.begin() + r + 1);
                int candidate_time = dp[l].first + seg_max;
                if (candidate_time < dp[i].first) {
                    dp[i].first = candidate_time;
                    dp[i].second = dp[l].second; dp[i].second.push_back(i);
                }
            }
        }
    }

    cout << "Total Time: " << dp[n].first << '\n';
    int prev = 0;
    for (int idx : dp[n].second) {
        for (int i = prev; i < idx; i++) {
            cout << names[i] << ' ';
        }
        cout << '\n';
        prev = idx;
    }
    return 0;
}
