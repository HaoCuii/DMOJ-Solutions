#include <bits/stdc++.h>
using namespace std;

int indeg[8];
vector<vector<int>> graph(8);
priority_queue<int, vector<int>, greater<int>> pq;

int main(){
    int a, b;
    while (cin >> a >> b && (a != 0 || b != 0)) {
        indeg[b]++;
        graph[a].push_back(b);
    }
    graph[1].push_back(7); indeg[7]++;
    graph[1].push_back(4); indeg[4]++;
    graph[2].push_back(1); indeg[1]++;
    graph[3].push_back(4); indeg[4]++;
    graph[3].push_back(5); indeg[5]++;

    for (int i = 1; i <= 7; i++) {
        if (indeg[i] == 0) {
            pq.push(i);
        }
    }

    vector<int> ans;
    while (!pq.empty()) {
        int v = pq.top(); pq.pop();
        ans.push_back(v);
        for (int u : graph[v]) {
            indeg[u]--;
            if (indeg[u] == 0) {
                pq.push(u);
            }
        }
    }

    if (ans.size() == 7) {
        for (int i : ans) {
            cout << i << ' ';
        }
    } else {
        cout << "Cannot complete these tasks. Going to bed.";
    }

    return 0;
}
