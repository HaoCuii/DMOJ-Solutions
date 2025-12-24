#include <bits/stdc++.h>
using namespace std;


struct DSU {
    vector<int> parent, rank;

    DSU(int n): parent(n), rank(n, 0) {
        for (int i = 0; i < n; ++i)
            parent[i] = i;
    }


    int find(int x) {
        if (parent[x] != x)
            parent[x] = find(parent[x]);
        return parent[x];
    }

    
    bool unite(int x, int y) {
        x = find(x);
        y = find(y);
        if (x == y) return false;
        if (rank[x] < rank[y])
            swap(x, y);
        parent[y] = x;
        if (rank[x] == rank[y])
            rank[x]++;
        return true;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<pair<double,double>> coords(n);
    for (int i = 0; i < n; ++i) {
        cin >> coords[i].first >> coords[i].second;
    }

    DSU uf(n);


    int m;
    cin >> m;
    for (int i = 0; i < m; ++i) {
        int u, v;
        cin >> u >> v;
        uf.unite(u - 1, v - 1);
    }

    vector<tuple<double,int,int>> edges;
    edges.reserve((size_t)n * (n - 1) / 2);

    for (int i = 0; i < n; ++i) {
        for (int j = i + 1; j < n; ++j) {
            double dx = coords[i].first - coords[j].first;
            double dy = coords[i].second - coords[j].second;
            double dist = sqrt(dx * dx + dy * dy);
            edges.emplace_back(dist, i, j);
        }
    }

    sort(edges.begin(), edges.end(), [](auto &a, auto &b) {
        return get<0>(a) < get<0>(b);
    });

    double total_length = 0.0;
    vector<pair<int,int>> new_cables;

    for (auto &e : edges) {
        double w;
        int u, v;
        tie(w, u, v) = e;
        if (uf.find(u) != uf.find(v)) {
            uf.unite(u, v);
            total_length += w;
            new_cables.emplace_back(u + 1, v + 1); 
        }
    }

    cout << fixed << setprecision(2) << total_length << "\n";
    for (auto &c : new_cables) {
        cout << c.first << " " << c.second << "\n";
    }

    return 0;
}
