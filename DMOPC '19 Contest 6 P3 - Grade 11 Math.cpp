#include <iostream>
#include <vector>
#include <set>
using namespace std;

using ll = long long;

int main() {
    int ls, m;
    cin >> ls >> m;

    string s;
    cin >> s;

    const ll mod = 1e9 + 7;
    vector<ll> pow = {1};
    set<int> zeros;

    for (int i = 1; i <= ls; i++) {
        pow.push_back((pow[i - 1] * 2LL) % mod);
    }

    ll ans = 0;
    for (int i = 0; i < ls; i++) {
        if (s[i] == '0') {
            zeros.insert(i);
        } else {
            ans = (ans + pow[ls - 1 - i]) % mod;
        }
    }

    for (int i = 0; i < m; i++) {
        int l, r;
        cin >> l >> r;

        auto lower = zeros.lower_bound(l - 1);
        while (lower != zeros.end() && *lower <= r - 1) {
            ans = (ans + pow[ls - 1 - *lower]) % mod;
            zeros.erase(lower++);
        }

        cout << ans << '\n';
    }

    return 0;
}