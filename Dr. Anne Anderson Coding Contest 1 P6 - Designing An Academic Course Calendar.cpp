#include <bits/stdc++.h>
using namespace std;

const int maxn = 200001;

set<int> want, needed;
int indeg[maxn];
vector<vector<int>> graph(maxn), rev_graph(maxn);
priority_queue<int, vector<int>, greater<int>> pq;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;

    vector<int> wanted(k);
    for (int i = 0; i < k; i++) {
        cin >> wanted[i];
        want.insert(wanted[i]);
    }

    vector<pair<int,int>> edges(m);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        edges[i] = {a, b};
        rev_graph[b].push_back(a);
    }

    vector<bool> visited(n+1,false);
    for (int x : wanted) {
        if (!visited[x]) {
            stack<int> st;
            st.push(x);
            while (!st.empty()) {
                int v = st.top(); st.pop();
                if (visited[v]) continue;
                visited[v] = true;
                needed.insert(v);
                for (int u : rev_graph[v]) {
                    if (!visited[u]) st.push(u);
                }
            }
        }
    }

    for (auto &e : edges) {
        int a = e.first, b = e.second;
        if (needed.count(a) && needed.count(b)) {
            graph[a].push_back(b);
            indeg[b]++;
        }
    }

    for (int i = 1; i <= n; i++) {
        if (needed.count(i) && indeg[i] == 0) {
            pq.push(i);
        }
    }

    vector<vector<int>> ans;
    while (!pq.empty() && !want.empty()) {
        vector<int> sem;
        while (!pq.empty()) {
            int v = pq.top(); pq.pop();
            if (want.count(v)) want.erase(v);
            sem.push_back(v);
        }
        for (int v : sem) {
            for (int u : graph[v]) {
                if (--indeg[u] == 0) {
                    pq.push(u);
                }
            }
        }
        if (!sem.empty()) {
            ans.push_back(sem);
        }
    }

    cout << ans.size() << "\n";
    for (auto &sem : ans) {
        for (int v : sem) {
            cout << v << " ";
        }
        cout << "\n";
    }

    return 0;
}
