#include <bits/stdc++.h>
using namespace std;

using ll = long long;
const int MAXN = 262150;
int n, arr[MAXN];
pair<int,ll> seg[4 * MAXN];

void build(int v, int tl, int tr){
    if (tl == tr){
        seg[v] = {arr[tl], 0};
    } else {
        int tm = (tl + tr) / 2;
        build(v*2, tl, tm);
        build(v*2 + 1, tm+1, tr);
        ll diff = 1LL * (seg[v*2].first - seg[v*2+1].first) * (seg[v*2].first - seg[v*2+1].first);
        seg[v] = {
            max(seg[v*2].first, seg[v*2+1].first),
            seg[v*2].second + seg[v*2+1].second + diff
        };
    }
}

void update(int v, int tl, int tr, int pos, int new_val){
    if (tl == tr){
        seg[v] = {new_val, 0};
    } else {
        int tm = (tl + tr) / 2;
        if (pos <= tm)
            update(v*2, tl, tm, pos, new_val);
        else
            update(v*2 + 1, tm+1, tr, pos, new_val);
        ll diff = 1LL * (seg[v*2].first - seg[v*2+1].first) * (seg[v*2].first - seg[v*2+1].first);
        seg[v] = {
            max(seg[v*2].first, seg[v*2+1].first),
            seg[v*2].second + seg[v*2+1].second + diff
        };
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    vector<int> B(n-1);
    vector<bool> present(n+1, false);
    for(int i = 0; i < n-1; i++){
        cin >> B[i];
        present[B[i]] = true;
    }
    int x = 1;
    while(x <= n && present[x]) x++;
    arr[1] = x;
    for(int i = 2; i <= n; i++){
        arr[i] = B[i-2];
    }
    build(1, 1, n);
    vector<ll> ans(n+1);
    for(int i = 1; i <= n; i++){
        ans[i] = seg[1].second;
        if(i < n){
            int bval = B[i-1];
            update(1, 1, n, i, bval);
            update(1, 1, n, i+1, x);
        }
    }
    for(int i = 1; i <= n; i++){
        cout << ans[i] << (i < n ? ' ' : '\n');
    }
    return 0;
}
