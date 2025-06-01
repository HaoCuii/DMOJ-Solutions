#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const int MAXN = 200010;
int n, q;
ll arr[MAXN];

struct Node {
    ll total_sum;
    ll max_prefix_sum;
};

Node seg[4 * MAXN];

Node combine(const Node &left, const Node &right) {
    Node res;
    res.total_sum = left.total_sum + right.total_sum;
    res.max_prefix_sum = max(left.max_prefix_sum, left.total_sum + right.max_prefix_sum);
    return res;
}

void build(int v, int tl, int tr) {
    if (tl == tr) {
        seg[v].total_sum = arr[tl];
        seg[v].max_prefix_sum = arr[tl];
    } else {
        int tm = (tl + tr) / 2;
        build(v * 2, tl, tm);
        build(v * 2 + 1, tm + 1, tr);
        seg[v] = combine(seg[v * 2], seg[v * 2 + 1]);
    }
}

Node query(int v, int tl, int tr, int l, int r) {
    if (l > r) return {0, LLONG_MIN}; 
    if (tl == l && tr == r) return seg[v];
    int tm = (tl + tr) / 2;
    if (r <= tm) {
        return query(v * 2, tl, tm, l, r);
    } else if (l > tm) {
        return query(v * 2 + 1, tm + 1, tr, l, r);
    } else {
        Node leftPart = query(v * 2, tl, tm, l, tm);
        Node rightPart = query(v * 2 + 1, tm + 1, tr, tm + 1, r);
        return combine(leftPart, rightPart);
    }
}

void update(int v, int tl, int tr, int pos, ll new_val) {
    if (tl == tr) {
        seg[v].total_sum = new_val;
        seg[v].max_prefix_sum = new_val;
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v * 2, tl, tm, pos, new_val);
        else
            update(v * 2 + 1, tm + 1, tr, pos, new_val);
        seg[v] = combine(seg[v * 2], seg[v * 2 + 1]);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> q;
    for (int i = 0; i < n; i++) cin >> arr[i];
    build(1, 0, n - 1);

    while (q--) {
        char type;
        cin >> type;
        if (type == 'P') {
            int l, r;
            cin >> l >> r;
            l--; r--;
            Node ans = query(1, 0, n - 1, l, r);
            cout << ans.max_prefix_sum << "\n";
        } else if (type == 'U') {
            int i;
            ll x;
            cin >> i >> x;
            i--;
            update(1, 0, n - 1, i, x);
        }
    }
    return 0;
}
