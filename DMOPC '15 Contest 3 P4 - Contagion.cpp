#include <bits/stdc++.h>
using namespace std;
using ll = long long;

vector<pair<int,int>> cities;
int n, x, q;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    for(int i = 0; i < n; i++){
        int a, b;
        cin >> a >> b;
        cities.emplace_back(a, b);
    }
    cin >> x;
    --x;

    const ll INF = LLONG_MAX;
    vector<ll> dist(n, INF);
    vector<char> seen(n, 0);
    dist[x] = 0;

    for(int it = 0; it < n; it++){
        int u = -1;
        ll best = INF;
        for(int i = 0; i < n; i++){
            if(!seen[i] && dist[i] < best){
                best = dist[i];
                u = i;
            }
        }
        if(u == -1) break; seen[u] = 1;
        for(int v = 0; v < n; v++){
            if(seen[v]) continue;
            ll dx = cities[u].first  - cities[v].first;
            ll dy = cities[u].second - cities[v].second;
            dist[v] = min(dist[v], dist[u] + dx*dx + dy*dy);
        }
    }

    sort(dist.begin(), dist.end());

    cin >> q;
    while(q--){
        ll T;
        cin >> T;
        int ans = upper_bound(dist.begin(), dist.end(), T) - dist.begin();
        cout << ans << "\n";
    }

    return 0;
}
