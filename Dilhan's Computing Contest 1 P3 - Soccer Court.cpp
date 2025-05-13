#include <bits/stdc++.h>
using namespace std;

// Loop through all left and right cols
// Compute difference of left and right rectangles for each row
// Find the longest contiguous subarray where the sum is 0
// Time complexity: O(nm^2)

using ll = long long;
ll psa[800][401], field[800][400]; 

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    ll n, m; cin >> n >> m;
    for (ll i = 0; i < n; i++) {
        for (ll j = 0; j < m; j++) {
            cin >> field[i][j];
        }
    }
    for (ll i = 0; i < n; i++) {
        psa[i][0] = 0;
        for (ll j = 0; j < m; j++) {
            psa[i][j + 1] = psa[i][j] + field[i][j]; 
        }    
    }
    ll big = 0;
    for (ll r = 2;  r <= m; r++) {
        for (ll l = 1; l < r; l++) {
            if ((r - l + 1) % 2 == 1) continue;
            ll mid = (l + r) / 2;
            map<ll, ll> freq = {{0, 0}}; // each key stores first occurrence
            vector<ll> diff(n + 1, 0);

            for (ll i = 0; i < n; i++) {
                ll suml = psa[i][mid] - psa[i][l - 1];
                ll sumr = psa[i][r] - psa[i][mid];
                diff[i + 1] = diff[i] + (sumr - suml);
                freq.try_emplace(diff[i + 1], i + 1);
            }
            for (ll i = 1; i <= n; i++) {
                ll h = freq[diff[i]];
                big = max(big, (i - h) * (r - l + 1));
            }
        }
    }
    cout << big;
    return 0;
}