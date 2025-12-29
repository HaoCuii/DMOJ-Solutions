#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <climits>

using namespace std;

int main() {
    int nodes, edges;
    cin >> nodes >> edges;

    vector<vector<pair<int, int>>> graph(nodes + 1);

    for (int i = 0; i < edges; ++i) {
        int a, b, l;
        cin >> a >> b >> l;
        graph[a].push_back({b, l});
        graph[b].push_back({a, l});
    }

    vector<int> dist(nodes + 1, INT_MAX);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> queue;
    queue.push({0, 1});
    dist[1] = 0;

    while (!queue.empty()) {
        auto top = queue.top();
        queue.pop();
        int l = top.first, n = top.second;
        if (l > dist[n])
            continue;
        for (auto it = graph[n].begin(); it != graph[n].end(); ++it) {
            int neighbor = it->first, length = it->second;
            if (l + length < dist[neighbor]) {
                dist[neighbor] = l + length;
                queue.push({dist[neighbor], neighbor});
            }
        }
    }

    int shortest = dist[nodes];

    vector<pair<int, int>> distPair(nodes + 1, {INT_MAX, INT_MAX});
    queue.push({0, 1});

    while (!queue.empty()) {
        auto top = queue.top();
        queue.pop();
        int l = top.first, n = top.second;
        int val = -1;
        for (auto it = graph[n].begin(); it != graph[n].end(); ++it) {
            int neighbor = it->first, length = it->second;
            if (neighbor == nodes)
                val = shortest;
            if (l + length < distPair[neighbor].first && l + length) {
                if (distPair[neighbor].first > val)
                    distPair[neighbor].second = distPair[neighbor].first;
                distPair[neighbor].first = l + length;
                queue.push({distPair[neighbor].first, neighbor});
            } else if (l + length < distPair[neighbor].second && l + length > val) {
                distPair[neighbor].second = l + length;
                queue.push({distPair[neighbor].second, neighbor});
            }
        }
    }

    if (distPair[nodes].second == INT_MAX)
        cout << -1 << endl;
    else
        cout << distPair[nodes].second << endl;

    return 0;
}