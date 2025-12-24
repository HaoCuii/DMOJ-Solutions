#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const ll MAXN = 1000010;
const ll MOD = 1000003;
ll n;
pair<ll, ll> arr[MAXN];

struct Node {
    ll start;
    ll duration;
};

Node seg[4 * MAXN];

Node merge(const Node& left, const Node& right) {
    if (left.start == -1LL) return right;
    if (right.start == -1LL) return left;

    return {max(left.start + left.duration, right.start) - left.duration, left.duration + right.duration};
}

void update(ll v, ll tl, ll tr, ll pos, ll new_val) {
    if (tl == tr) {
        seg[v].duration += new_val;
        if (seg[v].duration == 0LL) {
            seg[v] = Node{-1LL, 0LL};
        } else {
            seg[v] = Node{pos, seg[v].duration};
        }
    } else {
        ll tm = (tl + tr) / 2;
        if (pos <= tm)
            update(2 * v + 1, tl, tm, pos, new_val);
        else
            update(2 * v + 2, tm + 1, tr, pos, new_val);
        seg[v] = merge(seg[2 * v + 1], seg[2 * v + 2]);
    }
}

ll ans = 0;
ll insertion = 0;

int main() {
    fill(seg, seg + 4 * MAXN, Node{-1LL, 0LL});
    cin >> n;
    vector<ll> results;

    for (ll idx = 0; idx < n; idx++) {
        char qi;
        cin >> qi;
        if (qi == 'A') {
            ll s, t;
            cin >> s >> t;
            s = (s + ans) % MOD;
            t = (t + ans) % MOD;
            arr[insertion] = {s, t};
            insertion++;
            update(0, 0, MAXN - 1, s, t);
        } else {
            ll ip;
            cin >> ip;
            ll i = (ip + ans - 1 + MOD) % MOD;
            update(0, 0, MAXN - 1, arr[i].first, -arr[i].second);
        }

        auto [start, duration] = seg[0];
        ll result = start + duration - 1;
        cout << result << '\n';
        ans = result;
    }
    return 0;
}
