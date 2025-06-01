#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const int MAXN = 200010;
int n, q;
ll arr[MAXN];
ll seg[4 * MAXN];

// Build the segment tree for sum
void build(int v, int tl, int tr) {
    if (tl == tr) {
        seg[v] = arr[tl];
    } else {
        int tm = (tl + tr) / 2;
        build(v*2, tl, tm);
        build(v*2+1, tm+1, tr);
        seg[v] = seg[v*2] + seg[v*2+1];
    }
}

// Update the value at position pos to new_val
void update(int v, int tl, int tr, int pos, ll new_val) {
    if (tl == tr) {
        seg[v] = new_val;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v*2, tl, tm, pos, new_val);
        else
            update(v*2+1, tm+1, tr, pos, new_val);
        seg[v] = seg[v*2] + seg[v*2+1];
    }
}

// Query sum on range [l, r]
ll query(int v, int tl, int tr, int l, int r) {
    if (l > r) 
        return 0;
    if (tl == l && tr == r) {
        return seg[v];
    }
    int tm = (tl + tr) / 2;
    return query(v*2, tl, tm, l, min(r, tm)) + 
           query(v*2+1, tm+1, tr, max(l, tm+1), r);
}

// To find prefix sum from 0 to r, just call query(1, 0, n-1, 0, r)

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> q;
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    build(1, 0, n - 1);

    for (int i = 0; i < q; i++) {
        char type; 
        cin >> type;
        if (type == 'P') {
            int l,r; 
            cin >> l >> r;
            // prefix sum from 0 to r-1 (1-based input)
            cout << query(1, 0, n - 1, 0, r - 1) << "\n";
            cout << query(1, 0, n - 1, l - 1, r - 1) << "\n";
        } else {
            int pos; ll x; 
            cin >> pos >> x;
            update(1, 0, n - 1, pos - 1, x);
        }
    }

    return 0;
}
