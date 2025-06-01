#include <bits/stdc++.h>
using namespace std;

int n, m;
using ll = long long;


ll mindist(const set<int>& prev, int v, const vector<ll>& dist) {
    ll res = LLONG_MAX;
    auto it = prev.lower_bound(v);
    if (it != prev.end()) res = min(res, dist[*it] + abs(*it - v));
    if (it != prev.begin()) {
        --it;
        res = min(res, dist[*it] + abs(*it - v));
    }
     return res;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n >> m;
    vector<vector<int>> pos(m+1);
    for (int i = 0; i < n; i++) {
        int x; 
        cin >> x;
        pos[x].push_back(i);
    }

    vector<ll> dist(n, LLONG_MAX);
    set<int> prev;
    for (int i: pos[1]){
        dist[i] = i; 
        prev.insert(i);
    }

    for (int i = 2;  i <= m; i++){
        set<int> curr;
        for (int v: pos[i]) {
            dist[v] = mindist(prev, v, dist);
            curr.insert(v);
        }
        prev = curr;
    }

    ll ans = LONG_LONG_MAX;
    for (int v: pos[m]){
        ans = min(ans, dist[v]);
    }
    cout << ans+1 << '\n';
    return 0;
    }
