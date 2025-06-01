#include <bits/stdc++.h>
using namespace std;

int n, m, k;
long long build[31];
int cnt[31];

typedef tuple<int, long long, int> T;
auto cmp = [](const T& a, const T& b) {
    return get<1>(a) > get<1>(b); 
};
priority_queue<T, vector<T>, decltype(cmp)> pq(cmp);

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cin >> n >> m >> k;

    vector<unordered_set<int>> city(n + 1);
    vector<vector<pair<int, int>>> graph(n + 1);
    for (int i = 1; i <= k; i++) cin >> build[i];
    for (int i = 1; i <= k; i++) cin >> cnt[i];
    for (int i = 1; i <= k; i++) {
        for (int j = 0; j < cnt[i]; j++) {
            int x; cin >> x;
            city[x].insert(i);  
        }
    }
    for (int i = 0; i < m; i++) {
        int a, b, c; cin >> a >> b >> c;
        graph[a].emplace_back(b, c);
        graph[b].emplace_back(a, c);
    }
    vector<vector<long long>> dist(k + 1, vector<long long>(n + 1, LLONG_MAX));
    dist[0][1] = 0;
    pq.push({0, 0, 1}); //item, distance, node

    while (!pq.empty()) {
        auto [i, w, v] = pq.top(); pq.pop();
        if (w > dist[i][v]) continue;

        if (i + 1 <= k && city[v].count(i + 1)) {
            if (w < dist[i + 1][v]) {
                dist[i + 1][v] = w;
                pq.push({i + 1, w, v});
            }
        }
        for (auto [u, c] : graph[v]) {
            long long d = w + c;
            if (city[u].count(i + 1)) {
                if (d < dist[i + 1][u]) {
                    dist[i + 1][u] = d;
                    pq.push({i + 1, d, u});
                }
            }
            if (d < dist[i][u]) {
                dist[i][u] = d;
                pq.push({i, d, u});
            }
        }   
        // handle building an item
        if (i + 1 <= k && w + build[i + 1] < dist[i + 1][v]) {
            dist[i + 1][v] = w + build[i + 1];
            pq.push({i + 1, dist[i + 1][v], v});
        }
    }

    long long ans = LLONG_MAX;
    for (long long x : dist[k]) {
        ans = min(ans, x);
    }
    cout << ans << "\n";

    return 0;
}
