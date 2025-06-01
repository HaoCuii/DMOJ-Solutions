#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const int MAXN = 200010;
ll arr[MAXN], seg[4 * MAXN];
int n, q;

void build(int v, int tl, int tr) {
    if (tl == tr) {
        seg[v] = arr[tl];
    } else {
        int tm = (tl + tr) / 2;
        build(v * 2, tl, tm);
        build(v * 2 + 1, tm + 1, tr);
        seg[v] = seg[v * 2] + seg[v * 2 + 1];
    }
}

ll sum(int v, int tl, int tr, int l, int r) {
    if (l > r) return 0;
    if (tl == l && tr == r) return seg[v];
    int tm = (tl + tr) / 2;
    return sum(v * 2, tl, tm, l, min(r, tm)) +
           sum(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r);
}

void update(int v, int tl, int tr, int pos, ll new_val) {
    if (tl == tr) {
        seg[v] = new_val;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v * 2, tl, tm, pos, new_val);
        else
            update(v * 2 + 1, tm + 1, tr, pos, new_val);
        seg[v] = seg[v * 2] + seg[v * 2 + 1];
    }
}

int main() {
    cin >> n >> q;
    for (int i = 0; i < n; i++) cin >> arr[i];
    build(1, 0, n - 1);

    for (int i = 0; i < q; i++) {
        char qi;
        cin >> qi;
        if (qi == 'S') {
            int l, r;
            cin >> l >> r;
            cout << sum(1, 0, n - 1, l - 1, r - 1) << '\n';
        } else if (qi == 'U') {
            int i;
            ll x;
            cin >> i >> x;
            update(1, 0, n - 1, i - 1, x);
        }
    }
    return 0;
}
