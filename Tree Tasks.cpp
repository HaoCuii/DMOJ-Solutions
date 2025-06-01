#include <bits/stdc++.h>
using namespace std;

vector<vector<pair<int, int>>> graph;
vector<bool> visited;
vector<int> currentPath, longestPath;
vector<int> psa;
int maxDist = 0;

void dfs(int node, int dist) {
    visited[node] = true;
    currentPath.push_back(node);
    if (dist > maxDist) {
        maxDist = dist;
        longestPath = currentPath;
    }
    for (auto [neighbor, weight] : graph[node]) {
        if (!visited[neighbor]) {
            dfs(neighbor, dist + weight);
        }
    }
    currentPath.pop_back();
    visited[node] = false;
}

int main() {
    int n;
    cin >> n;
    graph.resize(n + 1);
    visited.resize(n + 1);
    for (int i = 0; i < n - 1; ++i) {
        int a, b, c;
        cin >> a >> b >> c;
        graph[a].emplace_back(b, c);
        graph[b].emplace_back(a, c);
    }

    dfs(1, 0);
    int farthest = longestPath.back();

    fill(visited.begin(), visited.end(), false);
    currentPath.clear();
    longestPath.clear();
    maxDist = 0;

    dfs(farthest, 0);

    psa.resize(longestPath.size());
    psa[0] = 0;
    for (int i = 1; i < longestPath.size(); ++i) {
        int u = longestPath[i - 1];
        int v = longestPath[i];
        for (auto [to, w] : graph[u]) {
            if (to == v) {
                psa[i] = psa[i - 1] + w;
                break;
            }
        }
    }
    int diameter = psa.back();
    int radius = INT_MAX;
    for (int i = 0; i < psa.size(); ++i) {
        int distFromStart = psa[i];
        int distFromEnd = diameter - distFromStart;
        radius = min(radius, max(distFromStart, distFromEnd));
    }

    cout << diameter << "\n";
    cout << radius << "\n";
    return 0;
}
